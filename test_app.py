
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_normal_search():
    response = client.get(
        "/lab/sqli/fixed",
        params={"q": "Mouse"},
    )

    assert response.status_code == 200
    assert [item["name"] for item in response.json()["results"]] == [
        "Mouse"
    ]


def test_sqli_vulnerable():
    response = client.get(
        "/lab/sqli/vulnerable",
        params={"q": "' OR 1=1 --"},
    )

    assert response.status_code == 200
    assert len(response.json()["results"]) == 3


def test_sqli_fixed():
    response = client.get(
        "/lab/sqli/fixed",
        params={"q": "' OR 1=1 --"},
    )

    assert response.status_code == 200
    assert response.json()["results"] == []
