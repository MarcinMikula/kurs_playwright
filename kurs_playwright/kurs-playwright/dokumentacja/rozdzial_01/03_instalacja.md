# Skrypt demonstracyjny: Uruchomienie Playwrighta i otwarcie strony
from playwright.sync_api import sync_playwright  # Import API synchronicznego Playwrighta

# Uruchomienie Playwrighta w bloku context managera
with sync_playwright() as p:
    # Uruchomienie przeglądarki Chromium w trybie headful (widoczna przeglądarka)
    browser = p.chromium.launch(headless=False)
    # Utworzenie nowej strony (karty) w przeglądarce
    page = browser.new_page()
    # Przejście na stronę example.com
    page.goto("https://example.com")
    # Pobranie tytułu strony i wyświetlenie go
    title = page.title()
    print(f"Tytuł strony: {title}")
    # Przeglądarka jest automatycznie zamykana po wyjściu z bloku `with`