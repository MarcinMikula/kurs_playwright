# Kurs Playwright

Witaj w repozytorium kursu Playwright! Ten projekt ma na celu naukę automatyzacji testów przeglądarek przy użyciu Playwrighta i pytest. Poniżej znajdziesz instrukcje instalacji, strukturę projektu oraz sposób uruchamiania testów i generowania raportów.


## Struktura projektu

- `dokumentacja/`: Pliki Markdown z opisem kursu.
  - `rozdzial_01/`: Podstawy Playwrighta (instalacja, podstawowe operacje, zaawansowane interakcje).
  - `rozdzial_02/`: Testy End-to-End (E2E, np. logowanie).
- `skrypty/`: Przykładowe skrypty demonstracyjne.
  - `rozdzial_01/`: Skrypty dla Rozdziału 1 (instalacja, operacje).
  - `rozdzial_02/`: Skrypty dla Rozdziału 2 (logowanie).
- `testy/`: Pliki testowe z użyciem pytest.
  - `test_instalacja.py`: Weryfikacja instalacji.
  - `test_podstawowe_operacje.py`: Test podstawowych operacji.
  - `test_zaawansowane_interakcje.py`: Test emulacji i zmian treści.
  - `test_logowanie.py`: Test logowania (Rozdział 2).
- `requirements.txt`: Zależności projektu.
- `pytest.ini`: Konfiguracja pytest.
- `generate_report.py`: Skrypt do generowania raportów z unikalnymi nazwami.
- `.gitignore`: Pliki do zignorowania (np. raporty HTML).

## Wymagania

- Python 3.11.0 lub nowszy.
- Playwright, pytest, pytest-playwright, pytest-html.

## Instalacja

1. Skonfiguruj wirtualne środowisko:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Na Windows
   pip install -r requirements.txt
   playwright install
   
2. Uruchamianie testów
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Na Windows
   pytest testy/test_zaawansowane_interakcje.py --headed --slowmo 500
   pytest testy/test_zaawansowane_interakcje.py --html=raport_test_zaawansowane_interakcje_$(Get-Date -Format "yyyyMMdd_HHmmss").html --self-contained-html





