def test_podstawowe_operacje(page):
    page.goto("https://the-internet.herokuapp.com/")
    page.wait_for_timeout(1000)
    assert page.title() == "The Internet"