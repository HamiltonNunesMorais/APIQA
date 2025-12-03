@echo off
color 0B
echo ====================================
echo 🧪 Running Automated Tests...
echo ====================================

call venv\Scripts\activate

pytest -vv --disable-warnings --html=reports/test_report.html --self-contained-html

echo.
echo 📌 Test results saved in /reports/test_report.html
echo ====================================
pause
