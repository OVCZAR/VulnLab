# VulnLab — lokalne laboratorium cyberbezpieczeństwa

VulnLab to projekt edukacyjny służący do nauki podstaw bezpieczeństwa aplikacji internetowych. Zawiera celowo podatne endpointy, ich zabezpieczone odpowiedniki oraz testy automatyczne, które pokazują różnice w działaniu obu wersji.

Projekt powstaje w celach edukacyjnych i portfolio z zakresu cyberbezpieczeństwa.

## Funkcjonalności

- **SQL Injection (SQLi)** — porównanie podatnego zapytania SQL z zapytaniem wykorzystującym parametry.
- **Cross-Site Scripting (XSS)** — demonstracja niebezpiecznego umieszczania danych użytkownika w HTML oraz ich bezpiecznego kodowania.
- **Testy automatyczne** — sprawdzanie zachowania endpointów podatnych i zabezpieczonych.
- **Raporty bezpieczeństwa** — dokumentacja wykrytych podatności, przebiegu testów i metod zabezpieczenia.

## Technologie

- Python
- FastAPI
- SQLite
- pytest
- HTML
- Git i GitHub

## Struktura projektu

```text
VulnLab/
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
├── .gitignore
└── docs/
    └── findings/
        ├── sqli.md
        └── xss.md
```

Lokalne pliki środowiska wirtualnego, baza danych i pliki cache nie są przeznaczone do publikowania w repozytorium.

## Wymagania

- Python 3.10 lub nowszy
- Git (opcjonalnie, jeśli projekt został już pobrany)
- Windows, Linux lub macOS

## Instalacja

Sklonuj repozytorium:

```bash
git clone https://github.com/OVCZAR/VulnLab.git
cd VulnLab
```

Utwórz środowisko wirtualne:

```bash
python -m venv .venv
```

Aktywuj środowisko.

Windows — PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Zainstaluj zależności:

```bash
python -m pip install -r requirements.txt
```

## Uruchomienie

Uruchom serwer lokalny:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Dokumentacja API będzie dostępna pod adresem:

http://127.0.0.1:8000/docs

Podstawowy endpoint kontrolny:

http://127.0.0.1:8000/health

## Dostępne endpointy

| Endpoint | Opis |
|---|---|
| `/` | Informacje o projekcie |
| `/health` | Kontrola działania aplikacji |
| `/lab/sqli/vulnerable` | Celowo podatne wyszukiwanie SQL |
| `/lab/sqli/fixed` | Wyszukiwanie z parametryzacją SQL |
| `/lab/xss/vulnerable` | Celowo podatne generowanie HTML |
| `/lab/xss/fixed` | Generowanie HTML z kodowaniem danych |

Endpointy wyszukiwania SQL przyjmują parametr `q`, a endpointy XSS parametr `name`.

## Testy automatyczne

Uruchom wszystkie testy:

```bash
python -m pytest -v
```

Testy obejmują m.in.:

- poprawność odpowiedzi endpointu kontrolnego;
- prawidłowe wyszukiwanie produktów;
- różnicę w zachowaniu podatnego i zabezpieczonego zapytania SQL;
- różnicę w sposobie umieszczania danych użytkownika w HTML.

## Zabezpieczenia

W zabezpieczonych wersjach zastosowano:

- parametryzację zapytań SQL, aby oddzielić kod SQL od danych wejściowych;
- kodowanie znaków specjalnych HTML, aby dane użytkownika nie były interpretowane jako znaczniki HTML lub kod skryptu.

Wersje podatne są celowym elementem laboratorium i służą wyłącznie do demonstracji problemów bezpieczeństwa.

## Raporty

Raporty dotyczące poszczególnych podatności znajdują się w katalogu `docs/findings/`.

- [SQL Injection](docs/findings/sqli.md)
- [Cross-Site Scripting (XSS)](docs/findings/xss.md)

## Bezpieczeństwo i zakres projektu

Projekt jest przeznaczony do nauki oraz testów na własnym, lokalnym środowisku.

**Nie należy udostępniać celowo podatnych endpointów publicznie ani wykorzystywać ich do testowania systemów bez zgody właściciela.**

## Status projektu

Projekt jest rozwijany. Kolejne planowane etapy obejmują rozszerzenie laboratorium o następne podatności, dodatkowe testy oraz dalsze uporządkowanie dokumentacji.