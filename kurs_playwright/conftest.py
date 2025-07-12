import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def browser(playwright: Playwright, request):
    browser_type = request.config.getoption("--browser", default="chromium")
    browser = getattr(playwright, browser_type).launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    context.add_cookies([{"name": "example", "value": "test", "domain": ".herokuapp.com", "path": "/"}])
    yield context

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()