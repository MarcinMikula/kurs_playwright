# Rozdział 2: Podstawy Frontendu
## 02 - Jak działają strony internetowe?

### Wprowadzenie
Strony internetowe opierają się na komunikacji między przeglądarką a serwerem za pomocą protokołu HTTP/HTTPS.

### Proces działania
1. **Żądanie**: Przeglądarka wysyła żądanie (np. GET) do serwera.
2. **Odpowiedź**: Serwer zwraca HTML, CSS i JavaScript.
3. **Renderowanie**: Przeglądarka buduje DOM i wykonuje skrypty.
4. **Interakcja**: Użytkownik klikając np. przycisk, wyzwala nowe żądania (AJAX, formularze).

### Przykład
Na The Internet logowanie wymaga wysłania danych formularza, co skutkuje zmianą URL na "/secure".

### Co dalej?
W następnym podrozdziale przejdziemy do testowania tych procesów za pomocą testów E2E.