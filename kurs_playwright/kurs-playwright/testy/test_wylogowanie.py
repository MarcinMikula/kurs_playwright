from playwright.sync_api import Page

def test_wylogowanie(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input[name='username']", "tomsmith")
    page.fill("input[name='password']", "SuperSecretPassword!")
    page.click("button[type='submit']")
    page.wait_for_url("**/secure")
    page.click("a[href='/logout']")
    page.wait_for_url("**/login")
    assert "login" in page.url
    message = page.text_content("div#flash.success")
    print(f"Komunikat po wylogowaniu: {message}")
    assert "You logged out" in message