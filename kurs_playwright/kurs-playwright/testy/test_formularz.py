from playwright.sync_api import Page

def test_formularz(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    initial_count = page.locator("button.added-manually").count()
    print(f"Początkowa liczba elementów: {initial_count}")
    page.click("button:has-text('Add Element')")
    print("Kliknięto Add Element")
    page.wait_for_selector("button.added-manually", state="attached", timeout=10000)
    new_count = page.locator("button.added-manually").count()
    print(f"Liczba elementów po dodaniu: {new_count}")
    assert new_count == initial_count + 1
    page.click("button.added-manually")
    final_count = page.locator("button.added-manually").count()
    print(f"Liczba elementów po usunięciu: {final_count}")
    assert final_count == initial_count