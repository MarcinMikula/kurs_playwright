# Skrypt demonstracyjny: Zaawansowane interakcje w Playwricie
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Emulacja iPhone'a
    iphone = p.devices["iPhone 12"]
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(**iphone)
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/")

    # Przechwytywanie sieci
    with page.expect_request("**/api/*") as request_info:
        page.click("text=Dynamic Content")
    request = request_info.value
    print(f"Żądanie sieciowe: {request.url}")

    # Zamknięcie
    browser.close()