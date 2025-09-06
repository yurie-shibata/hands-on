# hands-on

## Database Setup

Install dependencies:
```
pip install -r requirements.txt
```

Create the SQLite database and tables:
```
python db_setup.py
```

## API

Run the FastAPI application:
```
uvicorn app:app
```

Submit data to the API:
```
curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"Alice\"}" http://localhost:8000/api/submit
```
