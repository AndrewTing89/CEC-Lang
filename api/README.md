# CEC Lang - React + FastAPI Architecture

## Quick Start (Development)

### 1. Start the Backend
```bash
cd api
pip install fastapi uvicorn python-multipart
python main.py
```
Backend runs at: http://localhost:8000

### 2. Start the Frontend
```bash
cd interfaces/react-frontend
npm install
npm run dev
```
Frontend runs at: http://localhost:3000

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/ask` | POST | Send a question to the CEC Agent |
| `/transcribe` | POST | Transcribe audio to text (Groq Whisper) |
| `/clear` | POST | Clear conversation memory |
| `/health` | GET | Health check |

## Production Build

```bash
# Build frontend
cd interfaces/react-frontend && npm run build

# Run with Docker
docker build -t cec-lang .
docker run -p 8080:8080 \
  -e GROQ_API_KEY=your_key \
  -e GOOGLE_API_KEY=your_key \
  -e OPENSEARCH_HOST=your_host \
  cec-lang
```

## Deploy to Google Cloud Run

```bash
# One-time setup
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Deploy
gcloud builds submit --config cloudbuild.yaml \
  --substitutions=_GROQ_API_KEY="xxx",_GOOGLE_API_KEY="xxx",_OPENSEARCH_HOST="xxx"
```
