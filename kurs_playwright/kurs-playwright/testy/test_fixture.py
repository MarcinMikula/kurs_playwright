def test_fixture_with_context(page):
    page.goto("https://the-internet.herokuapp.com/")
    print(f"Tytuł strony: {page.title()}")
    assert page.title() == "The Internet"
    cookies = page.context.cookies()
    print(f"Ciasteczka: {cookies}")
    assert any(cookie["name"] == "example" for cookie in cookies)