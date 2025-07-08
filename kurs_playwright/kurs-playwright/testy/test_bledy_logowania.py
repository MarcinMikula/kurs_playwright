from playwright.sync_api import Page

def test_bledy_logowania(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input[name='username']", "zle_uzytkownik")
    page.fill("input[name='password']", "zle_haslo")
    page.click("button[type='submit']")
    message = page.text_content("div#flash.error")
    print(f"Komunikat błędu: {message}")
    assert "Your username is invalid!" in message or "Your password is invalid!" in message