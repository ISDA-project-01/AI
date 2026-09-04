@echo off
TITLE VAPIC PC1 Master Setup
echo ====================================================
echo      VAPIC - PC1 MASTER SETUP & LAUNCHER
echo ====================================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH!
    pause
    exit /b 1
)

if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat
echo Installing dependencies...
pip install -r requirements.txt

if not exist "jobs" mkdir jobs
if not exist "logs" mkdir logs
if not exist "shared" mkdir shared

echo Starting VAPIC Master Coordinator Gateway API...
set PORT=8000
python api.py
pause
