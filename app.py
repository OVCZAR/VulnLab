from pathlib import Path
import html
import sqlite3

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="VulnLab",
    description="Local web security training lab",
    version="0.2.0",
)

DB_PATH = Path(__file__).with_name("lab.db")


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)

        count = connection.execute(
            "SELECT COUNT(*) FROM products"
        ).fetchone()[0]

        if count == 0:
            connection.executemany(
                "INSERT INTO products (name) VALUES (?)",
                [
                    ("Laptop",),
                    ("Keyboard",),
                    ("Mouse",),
                ],
            )


initialize_database()


@app.get("/")
def home():
    return {
        "project": "VulnLab",
        "version": "0.2.0",
        "message": "Local web security training lab",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/lab/sqli/vulnerable")
def vulnerable_search(q: str = Query(default="")):
    # INTENTIONALLY VULNERABLE: local training only.
    sql = (
        "SELECT id, name FROM products "
        f"WHERE name LIKE '%{q}%' ORDER BY id"
    )

    with get_connection() as connection:
        rows = connection.execute(sql).fetchall()

    return {"results": [dict(row) for row in rows]}


@app.get("/lab/sqli/fixed")
def fixed_search(q: str = Query(default="")):
    # Parameterized query: input is treated as data.
    sql = """
        SELECT id, name FROM products
        WHERE name LIKE ? ORDER BY id
    """

    with get_connection() as connection:
        rows = connection.execute(
            sql, (f"%{q}%",)
        ).fetchall()

    return {"results": [dict(row) for row in rows]}


@app.get("/lab/xss/vulnerable", response_class=HTMLResponse)
def vulnerable_xss(name: str = ""):
    # INTENTIONALLY VULNERABLE: local training only.
    return HTMLResponse(
        f"""
        <!DOCTYPE html>
        <html lang="pl">
        <head><meta charset="UTF-8"><title>VulnLab - XSS</title></head>
        <body>
            <h1>Wersja podatna na XSS</h1>
            <p>Witaj, {name}!</p>
        </body>
        </html>
        """
    )


@app.get("/lab/xss/fixed", response_class=HTMLResponse)
def fixed_xss(name: str = ""):
    safe_name = html.escape(name)

    return HTMLResponse(
        f"""
        <!DOCTYPE html>
        <html lang="pl">
        <head><meta charset="UTF-8"><title>VulnLab - XSS</title></head>
        <body>
            <h1>Wersja zabezpieczona przed XSS</h1>
            <p>Witaj, {safe_name}!</p>
        </body>
        </html>
        """
    )
