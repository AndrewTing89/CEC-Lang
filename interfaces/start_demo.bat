@echo off
title CEC Lang Demo Launcher
echo ========================================
echo     CEC Lang Demo Launcher
echo ========================================
echo.
cd /d "%~dp0.."
echo Current directory: %CD%
echo.
echo Starting Streamlit (browser will open automatically)...
echo.
python -m streamlit run interfaces/streamlit_app.py
pause
