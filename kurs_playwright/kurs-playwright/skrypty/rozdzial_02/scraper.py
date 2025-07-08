from playwright.sync_api import sync_playwright

def scrape_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")
        links = page.query_selector_all("a")
        print("Znalezione linki:")
        for i, link in enumerate(links, 1):
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"{i}. {text} ({href})")
        page.wait_for_timeout(2000)
        browser.close()

if __name__ == "__main__":
    scrape_links()