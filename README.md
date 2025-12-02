python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
python app.py

GET http://localhost:8000/products

pytest -v

# 1 START THE API
cd app
uvicorn app:app --reload --port 8000

# 2  RUN POSTMAN NEWMAN TESTS
cd postmanTest
./run-tests.sh

# 3 RUN PYTEST
cd ..
.\venv\Scripts\activate
pytest -vv

