@echo off
cd /d "%~dp0"

echo Starting Cybersecurity Project...

docker compose up -d --build

if errorlevel 1 (
    echo Failed to start the project.
    pause
    exit /b 1
)

echo Project started!
start http://localhost:8080

pause
