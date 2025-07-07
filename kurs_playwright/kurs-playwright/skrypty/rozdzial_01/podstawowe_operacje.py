# Skrypt demonstracyjny: Podstawowe operacje w Playwricie
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    print(f"Tytuł strony: {page.title()}")

    # Wypełnienie pól logowania
    page.fill("input[name='username']", "tomsmith")
    page.fill("input[name='password']", "SuperSecretPassword!")

    # Kliknięcie przycisku logowania
    page.click("button[type='submit']")
    page.wait_for_url("**/secure")

    print(f"Aktualny URL po logowaniu: {page.url}")