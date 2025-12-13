"""
FastAPI Backend for CEC Lang
Provides REST API endpoints for the CEC Agent and voice transcription
"""
import os
import sys
from pathlib import Path
from typing import Optional
from io import BytesIO

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from groq import Groq

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.agent import CECAgent

# Initialize FastAPI app
app = FastAPI(
    title="CEC Lang API",
    description="California Electrical Code Assistant API",
    version="1.0.0"
)

# CORS middleware - allow React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev server
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize CEC Agent (singleton)
_agent: Optional[CECAgent] = None

def get_agent() -> CECAgent:
    """Get or create the CEC Agent instance"""
    global _agent
    if _agent is None:
        _agent = CECAgent(verbose=False)
    return _agent


# Request/Response Models
class AskRequest(BaseModel):
    question: str
    include_nec_comparison: bool = False


class AskResponse(BaseModel):
    answer: str
    tool_calls: list
    model: str
    duration_seconds: float


class TranscribeResponse(BaseModel):
    text: str


# API Endpoints
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "cec-lang-api"}


@app.post("/ask", response_model=AskResponse)
async def ask_question(request: AskRequest):
    """
    Ask a question about CEC 2022 or NEC 2023 electrical codes.

    Args:
        request: Contains the question and optional NEC comparison flag

    Returns:
        Answer with tool calls and metadata
    """
    try:
        agent = get_agent()
        result = agent.ask(
            request.question,
            force_nec_comparison=request.include_nec_comparison
        )

        return AskResponse(
            answer=result.get("answer", ""),
            tool_calls=result.get("tool_calls", []),
            model=result.get("model", "unknown"),
            duration_seconds=result.get("duration_seconds", 0)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/transcribe", response_model=TranscribeResponse)
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Transcribe audio to text using Groq Whisper.

    Args:
        file: Audio file (wav, mp3, webm, etc.)

    Returns:
        Transcribed text
    """
    try:
        # Read the uploaded file
        audio_bytes = await file.read()
        print(f"[Transcribe] Received file: {file.filename}, size: {len(audio_bytes)} bytes, content_type: {file.content_type}")

        if len(audio_bytes) == 0:
            raise HTTPException(status_code=400, detail="Empty audio file")

        # Initialize Groq client
        client = Groq()  # Uses GROQ_API_KEY from environment

        # Determine content type - use a supported format
        filename = file.filename or "recording.webm"
        content_type = file.content_type or "audio/webm"

        print(f"[Transcribe] Sending to Groq: filename={filename}, content_type={content_type}")

        # Groq API expects file as tuple: (filename, file_bytes, content_type)
        transcription = client.audio.transcriptions.create(
            file=(filename, audio_bytes, content_type),
            model="whisper-large-v3-turbo",
            response_format="text",
            language="en"
        )

        print(f"[Transcribe] Success! Result: {transcription[:100] if transcription else 'empty'}...")
        return TranscribeResponse(text=transcription.strip())

    except Exception as e:
        import traceback
        print(f"[Transcribe] ERROR: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")


@app.post("/clear")
async def clear_conversation():
    """Clear the agent's conversation memory"""
    try:
        agent = get_agent()
        agent.clear_memory()
        return {"status": "cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/questions")
async def get_questions():
    """
    Get all evaluation questions from the question bank.
    Parses the CEC2022_eval_simple-text.txt file.
    """
    try:
        questions_file = Path(__file__).parent.parent / "eval" / "standardized_llm-as-judge" / "CEC2022_eval_simple-text.txt"

        if not questions_file.exists():
            raise HTTPException(status_code=404, detail="Questions file not found")

        with open(questions_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse questions from the file
        questions = []
        blocks = content.split('--------------------------------------------------------------------------------')

        for block in blocks:
            block = block.strip()
            if not block or block.startswith('CEC 2022') or block.startswith('Total:') or block.startswith('==='):
                continue

            lines = block.split('\n')
            if len(lines) >= 1:
                # First line contains ID and question
                first_line = lines[0].strip()
                if '\t' in first_line:
                    parts = first_line.split('\t', 1)
                    q_id = parts[0].strip()
                    q_text = parts[1].strip() if len(parts) > 1 else ""
                else:
                    continue

                # Find expected answer
                expected = ""
                for line in lines[1:]:
                    if line.strip().startswith('EXPECTED ANSWER:'):
                        expected = line.replace('EXPECTED ANSWER:', '').strip()
                        break

                if q_id and q_text:
                    questions.append({
                        "id": q_id,
                        "question": q_text,
                        "expected_answer": expected
                    })

        return {"questions": questions, "total": len(questions)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Serve React static files in production
frontend_path = Path(__file__).parent.parent / "interfaces" / "react-frontend" / "dist"

# List of API routes to exclude from static file serving
API_ROUTES = {"/ask", "/transcribe", "/clear", "/health", "/questions"}

if frontend_path.exists():
    app.mount("/assets", StaticFiles(directory=frontend_path / "assets"), name="assets")

    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        """Serve React app for all non-API routes"""
        # Don't intercept API routes
        if f"/{full_path}" in API_ROUTES or full_path in API_ROUTES:
            raise HTTPException(status_code=404, detail="Not found")

        file_path = frontend_path / full_path
        if file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        return FileResponse(frontend_path / "index.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
