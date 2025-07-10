from playwright.sync_api import sync_playwright
from urllib.parse import urljoin

def scrape_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/", wait_until="networkidle")  # Czekaj na pełne załadowanie
        base_url = "https://the-internet.herokuapp.com/"  # Bazowy URL do łączenia
        links = page.query_selector_all("a")
        print("Znalezione linki:")
        for i, link in enumerate(links, 1):
            href = link.get_attribute("href")
            if href:  # Ignoruj linki bez href
                full_url = urljoin(base_url, href)  # Konwertuj względne URL-e
                text = link.inner_text().strip()  # Usuń białe znaki
                if text:  # Wyświetl tylko linki z tekstem
                    print(f"{i}. {text} ({full_url})")
        page.wait_for_timeout(2000)
        browser.close()

if __name__ == "__main__":
    scrape_links()