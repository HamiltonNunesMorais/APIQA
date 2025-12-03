@echo off
color 0E
echo ====================================
echo 🚀 Starting FastAPI (dev mode)...
echo ====================================

cd app

call ..\venv\Scripts\activate

uvicorn app:app --reload

cd ..
