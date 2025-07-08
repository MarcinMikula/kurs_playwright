from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    initial_count = page.locator("button.added-manually").count()
    print(f"Początkowa liczba elementów: {initial_count}")
    page.click("button:has-text('Add Element')")
    print("Kliknięto Add Element")
    page.wait_for_selector("button.added-manually", state="attached")
    print(f"Dodano element: {page.locator('button.added-manually').count()} elementów")
    page.click("button.added-manually")
    print(f"Usunięto element: {page.locator('button.added-manually').count()} elementów")
    page.wait_for_timeout(2000)
    browser.close()