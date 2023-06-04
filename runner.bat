@echo off
title Spotified Runner

:: ASCII banner


:: Menu options
echo [1] Followers
echo [2] Likes
echo.

:: Prompt user for input
set /p choice="Enter a number from the list: "

:: Run Python file based on user's choice
if "%choice%"=="1" (
    python follower.py
) else if "%choice%"=="2" (
    python likes.py
) else (
    echo Invalid choice! Please select a valid number.
)

:: Pause at the end (optional)
pause
