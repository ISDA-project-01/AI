@echo off
TITLE VAPIC PC5 AI Peer Node Setup
echo ====================================================
echo      VAPIC - PC5 PEER NODE SETUP (DeepSeek)
echo ====================================================

call ..\venv\Scripts\activate.bat 2>nul || python -m venv venv && call venv\Scripts\activate.bat
pip install -r ..\requirements.txt

set NODE_PORT=8004
set NODE_MODEL=deepseek-r1:1.5b
echo Starting PC5 Node Server on port %NODE_PORT% with model %NODE_MODEL%...
python ..\node4.py
pause
