from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from main import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensaje" in response.json()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
