def test_lokalizatory(page):
    page.goto("https://the-internet.herokuapp.com/")
    add_remove_link = page.locator("text=Add/Remove Elements")
    assert add_remove_link.count() == 1
    print("Znaleziono link Add/Remove Elements")
    h2 = page.locator("css=h2").filter(has_text="Available Examples")
    h2.wait_for(state="visible", timeout=10000)
    assert h2.text_content() == "Available Examples"
    print("Znaleziono nagłówek Available Examples")
    link = page.locator("xpath=//a[contains(text(), 'Basic')]")
    assert link.count() >= 1
    print("Znaleziono link z 'Basic'")