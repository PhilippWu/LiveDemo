"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient
from fastapi_app.main import app

client = TestClient(app)


def test_health_endpoint():
    """Test that /health returns 200 and expected JSON."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_todos_endpoint():
    """Test that /todos returns 200 and expected JSON."""
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "demo"}]
