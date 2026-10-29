@echo off
setlocal
cd /d "%~dp0"
echo ============================================
echo   CampusConnect - starting setup
echo ============================================
where python >nul 2>nul
if errorlevel 1 (
  echo ERROR: Python not found. Install Python 3.10+ from https://www.python.org/downloads/ and select Add Python to PATH.
  pause
  exit /b 1
)
if not exist "venv\Scripts\python.exe" (
  echo Creating virtual environment...
  python -m venv venv
  if errorlevel 1 (echo Could not create venv.& pause & exit /b 1)
)
echo Installing required packages...
"venv\Scripts\python.exe" -m pip install --upgrade pip
"venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (echo Package installation failed. Check your internet connection.& pause & exit /b 1)
echo Applying database migrations...
"venv\Scripts\python.exe" manage.py migrate
if errorlevel 1 (echo Migration failed. See the error above.& pause & exit /b 1)
echo Checking project...
"venv\Scripts\python.exe" manage.py check
if errorlevel 1 (pause & exit /b 1)
echo.
echo Website is starting. Keep this window open.
echo Open http://127.0.0.1:8000/ in your browser.
echo Admin panel: http://127.0.0.1:8000/admin/
echo Press CTRL+C to stop the server.
echo.
"venv\Scripts\python.exe" manage.py runserver
pause
