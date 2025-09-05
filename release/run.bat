@echo off
echo Starting Git Account Manager Pro...
echo.
GitAccountManagerPro.exe
if errorlevel 1 (
    echo.
    echo Application encountered an error.
    echo Please check the console output for details.
    pause
)
