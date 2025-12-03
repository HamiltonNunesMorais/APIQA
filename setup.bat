@echo off
color 0A
echo ============================
echo 🔧 Setting up environment...
echo ============================

REM Check if venv exists
IF NOT EXIST venv (
    echo Creating virtual environment...
    python -m venv venv
) ELSE (
    echo Virtual environment already exists.
)

echo Activating environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ✅ Environment setup complete!
echo.
pause
