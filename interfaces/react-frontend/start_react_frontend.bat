@echo off
title CEC Lang React Frontend Launcher
echo ========================================
echo     CEC Lang React Frontend Launcher
echo ========================================
echo.

REM Navigate to project root
cd /d "%~dp0..\.."
echo Project directory: %CD%
echo.

REM Check if api/main.py exists
if not exist "api\main.py" (
    echo ERROR: api\main.py not found!
    echo Make sure you're running from the correct directory.
    pause
    exit /b 1
)

echo Installing backend dependencies...
pip install fastapi uvicorn python-multipart groq --quiet

echo.
echo Starting FastAPI backend (port 8000)...
start "CEC Lang API" cmd /k "cd /d "%CD%" && python api/main.py"

echo Waiting for backend to start...
timeout /t 5 /nobreak >nul

REM Verify backend is running
echo Checking if backend started...
netstat -ano | findstr :8000 | findstr LISTENING >nul
if errorlevel 1 (
    echo WARNING: Backend may not have started. Check the API window for errors.
) else (
    echo Backend is running on port 8000
)

echo.
echo Starting React frontend (port 3000)...
cd interfaces\react-frontend

REM Check if node_modules exists
if not exist "node_modules" (
    echo Installing dependencies...
    call npm install
) else (
    echo Dependencies already installed.
)

echo.
echo Starting development server...
echo Browser will open at http://localhost:3000
echo.
npm run dev

pause
