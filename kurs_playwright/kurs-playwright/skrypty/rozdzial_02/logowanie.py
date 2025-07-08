from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input[name='username']", "tomsmith")
    page.fill("input[name='password']", "SuperSecretPassword!")
    page.click("button[type='submit']")
    print(f"Zalogowano: {page.url}")
    page.wait_for_timeout(2000)  # Poczekaj, aby zobaczyć wynik
    browser.close()