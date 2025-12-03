@echo off
color 0D
echo ====================================
echo 📌 Running Postman Collection...
echo ====================================

call venv\Scripts\activate

cd postman

set timestamp=%DATE:/=-%_%TIME::=-%

newman run collections\postman_collection.json ^
    --env-var "BASE_URL=http://localhost:8000" ^
    --reporters cli,html ^
    --reporter-html-export results\results_%timestamp%.html

echo.
echo 📌 Newman test report saved. Check /postman/results/
echo ====================================
pause
