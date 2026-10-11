# VulnLab

**VulnLab** to lokalne laboratorium bezpieczeństwa aplikacji internetowych stworzone w Pythonie z wykorzystaniem FastAPI i SQLite. Projekt służy do praktycznej nauki wykrywania podatności oraz poznawania metod ich naprawiania.

Laboratorium pozwala porównywać celowo podatne implementacje z poprawionymi rozwiązaniami, a następnie sprawdzać ich działanie za pomocą testów automatycznych.

## Funkcjonalności

- Demonstracja podatności SQL Injection.
- Porównanie podatnego i poprawionego zapytania SQL.
- Lokalna baza danych SQLite z przykładowymi danymi.
- Interfejs API oparty na FastAPI.
- Automatyczne testy bezpieczeństwa z wykorzystaniem pytest.
- Interaktywna dokumentacja API dostępna przez Swagger UI.

## Wykorzystane technologie

- **Python** – język programowania.
- **FastAPI** – tworzenie interfejsu API.
- **SQLite** – lokalna baza danych.
- **Uvicorn** – serwer aplikacji.
- **pytest** – testy automatyczne.
- **HTTPX** – obsługa żądań HTTP w testach.

## Aktualny stan projektu

### Zrealizowane

- Podstawowe endpointy aplikacji.
- Endpoint sprawdzający stan serwera.
- Demonstracja SQL Injection.
- Poprawiona wersja zapytania wykorzystująca parametryzację.
- Testy automatyczne sprawdzające działanie obu implementacji.

### Planowany rozwój

- **XSS (Cross-Site Scripting)** – demonstracja nieprawidłowego przetwarzania treści użytkownika.
- **IDOR (Insecure Direct Object Reference)** – demonstracja błędów kontroli dostępu do zasobów.
- System zadań typu CTF z podpowiedziami i flagami.
- Interfejs graficzny laboratorium.
- Dokumentacja wykrytych podatności i sposobów ich naprawiania.
- Rozszerzenie zestawu testów bezpieczeństwa.

## Uruchomienie projektu

### 1. Utworzenie środowiska wirtualnego

W terminalu, w głównym katalogu projektu, wykonaj:

```powershell
python -m venv .venv
```

### 2. Aktywacja środowiska w systemie Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

Jeżeli PowerShell blokuje uruchamianie skryptów, należy rozwiązać ten problem zgodnie z konfiguracją lokalnego środowiska.

### 3. Instalacja wymaganych bibliotek

```powershell
python -m pip install -r requirements.txt
```

### 4. Uruchomienie aplikacji

```powershell
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Po uruchomieniu aplikacja będzie dostępna lokalnie.

Dokumentacja API:

http://127.0.0.1:8000/docs

## Uruchamianie testów

Aby uruchomić testy automatyczne, wykonaj:

```powershell
python -m pytest -v
```

Testy sprawdzają między innymi działanie podstawowych endpointów, prawidłowe wyszukiwanie produktów oraz różnice w zachowaniu podatnej i poprawionej implementacji SQL.

## Bezpieczeństwo

VulnLab zawiera celowo podatny kod przeznaczony wyłącznie do celów edukacyjnych.

- Uruchamiaj laboratorium w kontrolowanym środowisku lokalnym.
- Pozostaw serwer przypisany do adresu `127.0.0.1`.
- Nie wystawiaj podatnych endpointów do publicznego internetu.
- Nie testuj opisanych technik na systemach bez odpowiedniego upoważnienia.

## Cel projektu

Celem VulnLab jest rozwijanie praktycznych umiejętności z zakresu cyberbezpieczeństwa aplikacji internetowych, analizy podatności, bezpiecznego programowania i automatyzacji testów bezpieczeństwa.

Projekt jest rozwijany etapami, tak aby każda kolejna funkcjonalność obejmowała zarówno demonstrację problemu, jak i analizę sposobu jego rozwiązania.