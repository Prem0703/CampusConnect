@echo off
cd /d "%~dp0"
where code >nul 2>nul
if errorlevel 1 (
  echo VS Code command 'code' is not on PATH. Open VS Code, choose File ^> Open Folder, and select this folder.
  pause
  exit /b 1
)
code .
