# Test zgodny z pytest: Weryfikacja tytułu strony
from playwright.sync_api import Page

def test_podstawowa_nawigacja(page: Page):
    # Przejście na stronę example.com
    page.goto("https://the-internet.herokuapp.com/")
    # Weryfikacja tytułu strony
    assert page.title() == "The Internet"