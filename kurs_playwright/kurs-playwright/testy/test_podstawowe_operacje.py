# Test weryfikujący podstawowe operacje
from playwright.sync_api import Page

def test_podstawowe_operacje(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert page.title() == "The Internet"

    page.fill("input[name='username']", "tomsmith")
    page.fill("input[name='password']", "SuperSecretPassword!")
    page.click("button[type='submit']")
    page.wait_for_url("**/secure")

    assert "secure" in page.url