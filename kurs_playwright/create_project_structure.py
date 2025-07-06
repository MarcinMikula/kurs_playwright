import os
from pathlib import Path

# Główny folder projektu
project_root = "kurs-playwright"

# Struktura folderów i plików
structure = {
    "dokumentacja": {
        "rozdzial_01": [
            "01_wprowadzenie.md",
            "02_czym_jest_playwright.md",
            "03_instalacja.md"
        ],
        "rozdzial_02": [
            "01_czym_jest_frontend.md",
            "02_jak_dzialaja_strony.md",
            "03_testy_e2e.md"
        ],
        "rozdzial_03": [
            "01_podstawowe_operacje.md",
            "02_lokalizatory.md",
            "03_interakcje.md",
            "04_zaawansowane_funkcje.md"
        ],
        "rozdzial_04": [
            "01_konfiguracja_projektu.md",
            "02_strona_logowania.md",
            "03_pola_wyboru.md",
            "04_listy_rozwijane.md",
            "05_dynamiczna_tresc.md"
        ],
        "rozdzial_05": [
            "01_wprowadzenie_salesforce.md",
            "02_logowanie.md",
            "03_typowe_procesy.md",
            "04_najlepsze_praktyki.md"
        ]
    },
    "skrypty": {
        "rozdzial_01": ["instalacja_playwright.py"],
        "rozdzial_02": ["prosty_scraper.py"],
        "rozdzial_03": [
            "podstawowa_nawigacja.py",
            "przyklad_lokalizatory.py",
            "przyklad_interakcje.py",
            "zaawansowane_funkcje.py"
        ],
        "rozdzial_04": [
            "test_strony_logowania.py",
            "test_pola_wyboru.py",
            "test_listy_rozwijane.py",
            "test_dynamiczna_tresc.py"
        ],
        "rozdzial_05": [
            "test_logowanie_salesforce.py",
            "test_procesy_salesforce.py"
        ]
    },
    "testy": [
        "test_logowanie.py",
        "test_pola_wyboru.py"
    ]
}

# Zawartość wybranych plików
requirements_content = """playwright==1.44.0
pytest==8.3.2
pytest-playwright==0.5.1
"""

readme_content = """# Kurs Playwrighta

Kurs od podstaw do zaawansowanych zastosowań Playwrighta w automatyzacji testów E2E. Zawiera teorię (w folderze `dokumentacja/`) oraz praktyczne przykłady (w folderze `skrypty/`).

## Instalacja
1. Sklonuj repozytorium.
2. Zainstaluj zależności: `pip install -r requirements.txt`
3. Zainstaluj przeglądarki Playwrighta: `playwright install`
4. Uruchom testy: `pytest testy/`

## Struktura
- `dokumentacja/`: Teoria w plikach Markdown.
- `skrypty/`: Przykłady kodu z komentarzami.
- `testy/`: Testy automatyczne z użyciem pytest.
"""

gitignore_content = """__pycache__/
*.pyc
.pytest_cache/
playwright-report/
test-results/
"""

pytest_ini_content = """[pytest]
addopts = --headed --slowmo 500
"""

# Funkcja tworząca strukturę
def create_structure():
    # Utwórz główny folder projektu
    os.makedirs(project_root, exist_ok=True)

    # Utwórz pliki w głównym folderze
    with open(os.path.join(project_root, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write(requirements_content)
    with open(os.path.join(project_root, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    with open(os.path.join(project_root, ".gitignore"), "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    with open(os.path.join(project_root, "pytest.ini"), "w", encoding="utf-8") as f:
        f.write(pytest_ini_content)

    # Tworzenie folderów i plików w dokumentacji i skryptach
    for main_folder, subfolders in structure.items():
        os.makedirs(os.path.join(project_root, main_folder), exist_ok=True)
        if isinstance(subfolders, dict):
            for subfolder, files in subfolders.items():
                os.makedirs(os.path.join(project_root, main_folder, subfolder), exist_ok=True)
                for file in files:
                    Path(os.path.join(project_root, main_folder, subfolder, file)).touch()
        else:
            for file in subfolders:
                Path(os.path.join(project_root, main_folder, file)).touch()

    print(f"Struktura projektu '{project_root}' została utworzona!")

# Uruchomienie skryptu
if __name__ == "__main__":
    create_structure()