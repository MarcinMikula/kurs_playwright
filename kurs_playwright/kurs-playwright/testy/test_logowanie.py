from playwright.sync_api import Page

def test_logowanie(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input[name='username']", "tomsmith")
    page.fill("input[name='password']", "SuperSecretPassword!")
    page.click("button[type='submit']")
    page.wait_for_url("**/secure")
    assert "secure" in page.url
