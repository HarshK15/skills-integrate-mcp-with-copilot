from fastapi.testclient import TestClient
from src.app import app


client = TestClient(app)


def test_mcp_summary():
    resp = client.get("/mcp/summary")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "title" in data
    assert "endpoints" in data


def test_mcp_context():
    resp = client.get("/mcp/context")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # files key should exist (may be empty depending on environment)
    assert "files" in data


def test_activities_get():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # the example dataset includes Chess Club
    assert "Chess Club" in data
