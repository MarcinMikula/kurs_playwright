# Rozdział 2: Podstawy Frontendu
## 03 - Testy End-to-End (E2E)

### Wprowadzenie
Testy E2E symulują pełne scenariusze użytkownika, testując aplikację od początku do końca. W Playwricie pozwalają na automatyzację przeglądarek.

### Kluczowe operacje
- Nawigacja na stronę.
- Wypełnianie formularzy.
- Klikanie elementów.
- Weryfikacja wyników (np. zmiana URL, treść).

### Przykład
W folderze `testy/` znajdziesz `test_logowanie.py`, które testuje logowanie na The Internet. Skrypt demonstracyjny znajduje się w `skrypty/rozdzial_02/logowanie.py`.

### Krok po kroku
1. Uruchom skrypt `logowanie.py`:
   ```bash
   python skrypty/rozdzial_02/logowanie.py