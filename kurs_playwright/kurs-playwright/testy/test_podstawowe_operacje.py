# Test weryfikujący podstawowe operacje
import logging
from playwright.sync_api import Page

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_podstawowe_operacje(page: Page):
    logger.info("Rozpoczynam test podstawowych operacji")
    page.goto("https://the-internet.herokuapp.com/login")
    logger.info(f"Przejście na stronę: {page.url}")
    assert page.title() == "The Internet"

    page.fill("input[name='username']", "tomsmith")
    logger.info("Wypełniono pole username")
    page.fill("input[name='password']", "SuperSecretPassword!")
    logger.info("Wypełniono pole password")
    page.click("button[type='submit']")
    logger.info("Kliknięto przycisk logowania")
    page.wait_for_url("**/secure")

    assert "secure" in page.url
    logger.info("Test zakończony sukcesem")