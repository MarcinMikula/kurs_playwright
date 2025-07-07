# Test weryfikujący zaawansowane interakcje
from playwright.sync_api import Page

def test_zaawansowane_interakcje(page: Page):
    # Emulacja iPhone'a
    page.emulate_device("iPhone 12")
    page.goto("https://the-internet.herokuapp.com/")
    assert page.viewport_size["width"] == 390  # Rozdzielczość iPhone 12

    # Przechwytywanie sieci
    with page.expect_request("**/api/*") as request_info:
        page.click("text=Dynamic Content")
    request = request_info.value
    assert "api" in request.url