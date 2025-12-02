python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
python app.py

GET http://localhost:8000/products

pytest -v

# 1
cd app
uvicorn app:app --reload --port 8001

# 2  
cd postmanTest
./run-tests.sh

# 3 
cd pytest
pytest -vv
