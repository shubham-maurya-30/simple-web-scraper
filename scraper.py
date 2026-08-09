from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def scrape_books(url, status_callback=None):

    driver = webdriver.Chrome()

    try:
        if status_callback:
            status_callback("🌐 Opening website...")

        driver.get(url)

        if status_callback:
            status_callback("✓ Website opened successfully")

        # Give the page a moment to finish loading
        time.sleep(2)

        if status_callback:
            status_callback("🔎 Looking for books...")

        books = driver.find_elements(
            By.CLASS_NAME,
            "product_pod"
        )

        if not books:
            if status_callback:
                status_callback("⚠️ No books found on this page.")

            return []

        if status_callback:
            status_callback(
                f"✓ {len(books)} books found"
            )

        data = []

        if status_callback:
            status_callback("📥 Extracting data...")

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