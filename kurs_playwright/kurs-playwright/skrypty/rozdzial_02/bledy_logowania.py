from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input[name='username']", "zle_uzytkownik")
    page.fill("input[name='password']", "zle_haslo")
    page.click("button[type='submit']")
    print(f"Komunikat błędu: {page.text_content('div#flash.error')}")
    page.wait_for_timeout(2000)
    browser.close()