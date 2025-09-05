@echo off
echo Starting Git Account Manager Pro - Portable Launcher...
echo.
python portable_launcher.py
if errorlevel 1 (
    echo.
    echo Launcher encountered an error.
    echo Please ensure Python is installed and try again.
    pause
)
