@echo off
title CEC Lang - Stop Services
echo ========================================
echo     Stopping CEC Lang Services
echo ========================================
echo.

echo Stopping FastAPI backend (port 8000)...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000 ^| findstr LISTENING') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo Backend stopped.

echo.
echo Stopping React frontend (port 3000)...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :3000 ^| findstr LISTENING') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo Frontend stopped.

echo.
echo ========================================
echo     All services stopped
echo ========================================
echo.
pause
