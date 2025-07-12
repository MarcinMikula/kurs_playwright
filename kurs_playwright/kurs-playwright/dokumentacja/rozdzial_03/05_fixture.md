# Rozdział 3: Zaawansowane Techniki
## 05 - Fixture w Playwright

### Wprowadzenie
Fixture pozwalają na zarządzanie zasobami (np. przeglądarką, stroną) w testach. Używamy ich, aby uniknąć duplikowania kodu i zapewnić izolację.

### Kluczowe operacje
- Definiowanie fixture w `conftest.py`.
- Wstrzykiwanie fixture do testów.
- Zarządzanie cyklem życia (np. otwieranie/zamykanie przeglądarki).
- Dostosowanie kontekstu (np. ciasteczka, wybór przeglądarki).

### Przykład
Zobacz `testy/test_fixture.py` i `conftest.py`.

### Rozszerzenie
- Dodano parametr `--browser` do wyboru przeglądarki.
- Kontekst z ciasteczkami dla testów logowania.