@echo off
TITLE VAPIC PC2 AI Peer Node Setup
echo ====================================================
echo      VAPIC - PC2 PEER NODE SETUP (Qwen)
echo ====================================================

call ..\venv\Scripts\activate.bat 2>nul || python -m venv venv && call venv\Scripts\activate.bat
pip install -r ..\requirements.txt

set NODE_PORT=8001
set NODE_MODEL=qwen2.5-coder:3b
echo Starting PC2 Node Server on port %NODE_PORT% with model %NODE_MODEL%...
python ..\node1.py
pause
