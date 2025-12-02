python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
python app.py

GET http://localhost:8000/products

pytest -v
