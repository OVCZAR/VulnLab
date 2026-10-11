# Raport podatności: Cross-Site Scripting (XSS)

## 1. Cel testu

Celem testu było sprawdzenie, czy aplikacja poprawnie obsługuje dane użytkownika umieszczane w kodzie HTML.

## 2. Środowisko testowe

- Projekt: VulnLab
- Technologia: Python, FastAPI, HTML
- Środowisko: lokalne, `127.0.0.1`
- Typ podatności: Cross-Site Scripting (XSS)

## 3. Opis podatności

XSS to podatność polegająca na możliwości wykonania niepożądanego kodu JavaScript w przeglądarce użytkownika. Może wystąpić, gdy aplikacja umieszcza dane wejściowe w kodzie HTML bez odpowiedniego zabezpieczenia.

W projekcie przygotowano dwa endpointy: podatny oraz zabezpieczony.

## 4. Przebieg testu

Do parametru `name` przekazano następujący ciąg:

`<script>alert('XSS')</script>`

W wersji podatnej zawartość parametru została bezpośrednio umieszczona w HTML. Przeglądarka wykonała skrypt i wyświetliła okno dialogowe.

W wersji zabezpieczonej zastosowano funkcję `html.escape()`. Znaki specjalne zostały zamienione na encje HTML, dzięki czemu kod został wyświetlony jako tekst.

## 5. Wynik

Test potwierdził różnicę w zachowaniu obu endpointów:

- Wersja podatna umożliwiła wykonanie JavaScriptu.
- Wersja zabezpieczona wyświetliła przekazaną zawartość jako tekst.
- Testy automatyczne potwierdziły oczekiwane zachowanie obu wersji.

## 6. Sposób zabezpieczenia

Dane użytkownika należy odpowiednio kodować przed umieszczeniem ich w HTML. W projekcie wykorzystano `html.escape()`, które zabezpiecza znaki specjalne w kontekście tekstu HTML.

W bardziej rozbudowanych aplikacjach warto dodatkowo stosować bezpieczne szablony, unikać wstawiania danych do kontekstów JavaScript i atrybutów HTML oraz rozważyć politykę Content Security Policy (CSP).

## 7. Wnioski

Test pokazał, że nieprawidłowe umieszczanie danych użytkownika w HTML może prowadzić do wykonania kodu JavaScript. Odpowiednie kodowanie danych ogranicza to ryzyko. Porównanie obu endpointów oraz testy automatyczne pozwalają łatwo wykazać różnicę między implementacją podatną i zabezpieczoną.