@echo off
TITLE VAPIC Cluster Status Check
echo Checking VAPIC Master Status...
curl -s http://localhost:8000/api/status
echo.
pause
