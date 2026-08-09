from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def scrape_books(url, status_callback=None):

    chrome_options = Options()

    # Run Chrome without opening a visible browser window
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        options=chrome_options
    )

    try:

        if status_callback:
            status_callback("🌐 Opening website...")

        driver.get(url)

        if status_callback:
            status_callback(
                "✓ Website opened successfully"
            )

        # Give the page a moment to finish loading
        time.sleep(2)

        if status_callback:
            status_callback(
                "🔎 Looking for books..."
            )

        books = driver.find_elements(
            By.CLASS_NAME,
            "product_pod"
        )

        if not books:

            if status_callback:
                status_callback(
                    "⚠️ No books found on this page."
                )

            return []

        if status_callback:
            status_callback(
                f"✓ {len(books)} books found"
            )

        data = []

        if status_callback:
            status_callback(
                "📥 Extracting data..."
            )

        for book in books:

            title = book.find_element(
                By.TAG_NAME,
                "h3"
            ).find_element(
                By.TAG_NAME,
                "a"
            ).get_attribute("title")

            price = book.find_element(
                By.CLASS_NAME,
                "price_color"
            ).text

            data.append({
                "Title": title,
                "Price": price
            })

        if status_callback:
            status_callback(
                "✓ Data extraction completed"
            )

        return data

    finally:

        driver.quit()