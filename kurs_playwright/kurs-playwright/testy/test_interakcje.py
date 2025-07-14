def test_interakcje(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input[name='username']", "tomsmith")
    page.fill("input[name='password']", "SuperSecretPassword!")
    page.click("button[type='submit']")
    assert "secure" in page.text_content("div#flash")  # Twoja poprawka
    print("Logowanie powiodło się")