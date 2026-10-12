@echo off
chcp 65001 >nul
cd /d "%~dp0"
title MiniMax Video Automation Pipeline v1.0
echo ======================================================
echo    MiniMax Video Generation & Auto-Stitching Pipeline
echo ======================================================
echo
echo [1/3] Checking environment and configurations...
if not exist "config.ini" (
echo [ERROR] config.ini not found! Please check your configuration
pause
exit /b
)
if not exist "prompts.json" (
echo [ERROR] prompts.json not found! Please check your prompt file
pause
exit /b
)
echo [2/3] Launching generation pipeline...
python generator.py
echo
echo [3/3] Auto-stitching video segments with FFmpeg...
python pipeline_stitch.py
echo
echo ======================================================
echo    Pipeline execution completed successfully!
echo ======================================================
pause
