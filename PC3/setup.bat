@echo off
TITLE VAPIC PC3 AI Peer Node Setup
echo ====================================================
echo      VAPIC - PC3 PEER NODE SETUP (Gemma)
echo ====================================================

call ..\venv\Scripts\activate.bat 2>nul || python -m venv venv && call venv\Scripts\activate.bat
pip install -r ..\requirements.txt

set NODE_PORT=8002
set NODE_MODEL=gemma2:2b
echo Starting PC3 Node Server on port %NODE_PORT% with model %NODE_MODEL%...
python ..\node2.py
pause
