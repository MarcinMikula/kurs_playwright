# Test weryfikujący instalację Playwrighta
from playwright.sync_api import Page

def test_instalacja(page: Page):
    # Przejście na stronę testową
    page.goto("https://the-internet.herokuapp.com/")
    # Weryfikacja tytułu strony
    assert page.title() == "The Internet"
    # Weryfikacja, że strona się załadowała
    assert page.is_visible("text=Welcome to the-internet")