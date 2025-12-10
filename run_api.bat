@echo off
color 0E
echo ====================================
echo 🚀 Starting FastAPI (dev mode)...
echo ====================================

call venv\Scripts\activate

uvicorn app.main:app --reload


