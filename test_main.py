# app/test_main.py
from main import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, GitHub Actions with Docker!"