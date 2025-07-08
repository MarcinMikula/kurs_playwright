from playwright.sync_api import Page

def test_scraper(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    links = page.query_selector_all("a")
    print(f"Znaleziono {len(links)} linków")
    assert len(links) > 0  # Sprawdź, czy są jakiekolwiek linki