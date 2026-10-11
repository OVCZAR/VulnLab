
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


def test_vulnerable_normal_search():
    response = client.get(
        "/lab/sqli/vulnerable",
        params={"q": "Mouse"},
    )

    assert response.status_code == 200
    assert [item["name"] for item in response.json()["results"]] == [
        "Mouse"
    ]


def test_xss_vulnerable():
    payload = "<script>alert('XSS')</script>"

    response = client.get(
        "/lab/xss/vulnerable",
        params={"name": payload},
    )

    assert response.status_code == 200
    assert payload in response.text


def test_xss_fixed():
    payload = "<script>alert('XSS')</script>"

    response = client.get(
        "/lab/xss/fixed",
        params={"name": payload},
    )

    assert response.status_code == 200
    assert payload not in response.text
    assert "&lt;script&gt;" in response.text
