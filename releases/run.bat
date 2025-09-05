@echo off
title Git Account Manager Pro - Launcher
color 0A

echo.
echo ========================================
echo  Git Account Manager Pro v2.1.0
echo  Professional Git Account Management
echo ========================================
echo.
echo Starting application...
echo.

REM Check if executable exists
if not exist "GitAccountManagerPro.exe" (
    echo ERROR: GitAccountManagerPro.exe not found!
    echo Please ensure the executable is in the same folder.
    echo.
    pause
    exit /b 1
)

REM Run the application
echo Launching Git Account Manager Pro...
echo.
start "" "GitAccountManagerPro.exe"

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start the application.
    echo Please check if you have the required permissions.
    echo.
    pause
    exit /b 1
)

echo Application started successfully!
echo You can close this window now.
echo.
timeout /t 3 /nobreak >nul
exit /b 0
