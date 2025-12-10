@echo off
color 0A
echo ====================================
echo 🧪 Running Unit Tests...
echo ====================================

call venv\Scripts\activate

pytest tests/unit -vv --disable-warnings --html=reports/unit_report.html --self-contained-html

echo.
echo 📌 Unit test results saved in /reports/unit_report.html
echo ====================================
pause
