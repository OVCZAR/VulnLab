# Raport bezpieczeństwa — SQL Injection

## 1. Cel testu

Celem testu było sprawdzenie, czy dane przekazywane przez użytkownika mogą zmienić działanie zapytania SQL.

## 2. Badane endpointy

- `/lab/sqli/vulnerable` — wersja podatna na SQL Injection.
- `/lab/sqli/fixed` — wersja zabezpieczona.

## 3. Wykonany test

Użyto następującego ciągu testowego:

```text
' OR 1=1 --
```

Wysłano go jako parametr `q` do obu endpointów.

## 4. Wyniki

**Wersja podatna:** endpoint zwrócił wszystkie trzy produkty z bazy danych. Wprowadzone dane zmieniły logikę zapytania SQL.

**Wersja zabezpieczona:** endpoint zwrócił pustą listę. Dzięki parametryzacji wejście zostało potraktowane jako dane, a nie część instrukcji SQL.

## 5. Sposób zabezpieczenia

Zamiast łączyć dane użytkownika bezpośrednio z zapytaniem, zastosowano zapytanie parametryzowane:

```python
sql = """
    SELECT id, name FROM products
    WHERE name LIKE ? ORDER BY id
"""
rows = connection.execute(
    sql, (f"%{q}%",)
).fetchall()
```

## 6. Testy automatyczne

Testy sprawdzają poprawność endpointu zdrowia aplikacji, zwykłego wyszukiwania oraz zachowanie obu wersji endpointu wobec testowego ciągu SQL Injection.

Wynik: **4 testy zakończone powodzeniem**.

## 7. Wniosek

Test potwierdził podatność na SQL Injection w celowo niezabezpieczonym endpointcie szkoleniowym. Wersja wykorzystująca parametryzację nie wykazała tego zachowania w przeprowadzonym teście.

Wyniki dotyczą wyłącznie badanego środowiska lokalnego i nie stanowią potwierdzenia bezpieczeństwa całej aplikacji.
