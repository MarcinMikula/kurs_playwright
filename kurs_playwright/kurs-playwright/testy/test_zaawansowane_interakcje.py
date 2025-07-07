# Test weryfikujący zaawansowane interakcje
import pytest
from playwright.sync_api import Page, Browser, BrowserContext, Playwright

@pytest.fixture(scope="function")
def context_and_page(playwright: Playwright, browser: Browser) -> tuple[BrowserContext, Page]:
    # Emulacja iPhone 12
    iphone = playwright.devices["iPhone 12"]  # Dostęp do urządzeń przez playwright
    context = browser.new_context(**iphone)
    page = context.new_page()
    yield context, page
    context.close()

def test_zaawansowane_interakcje(context_and_page: tuple[BrowserContext, Page]):
    context, page = context_and_page
    # Przejście na stronę testową
    page.goto("https://the-internet.herokuapp.com/dynamic_content")
    assert page.viewport_size["width"] == 390  # Rozdzielczość iPhone 12

    # Zapisanie początkowej treści w div[class='large-10 columns']
    initial_content = page.text_content("div.large-10.columns").strip()

    # Kliknięcie, aby zaktualizować treść
    page.click("text=click here")  # Kliknij domyślny link zmieniający treść
    page.wait_for_timeout(2000)    # Zwiększ czas oczekiwania do 2 sekund

    # Weryfikacja zmiany treści
    new_content = page.text_content("div.large-10.columns").strip()
    assert initial_content != new_content, "Treść nie uległa zmianie po kliknięciu"
    assert len(new_content.split()) > 0, "Treść po kliknięciu jest pusta lub niezmieniona"