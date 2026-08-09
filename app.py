import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

from scraper import scrape_books


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Simple Web Scraper",
    page_icon="🕷️",
    layout="wide"
)


# =========================================================
# FILE SETTINGS
# =========================================================

HISTORY_FILE = "history.json"


# =========================================================
# HISTORY FUNCTIONS
# =========================================================

def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except:
        return []


def save_history(history):

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )


def add_to_history(url):

    history = load_history()

    # Remove duplicate URL
    history = [
        item for item in history
        if item["url"] != url
    ]

    new_item = {
        "url": url,
        "time": datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )
    }

    history.insert(0, new_item)

    save_history(history)


def delete_history(index):

    history = load_history()

    if 0 <= index < len(history):

        history.pop(index)

        save_history(history)


# =========================================================
# SESSION STATE
# =========================================================

if "scraped_data" not in st.session_state:
    st.session_state.scraped_data = []

if "activity" not in st.session_state:
    st.session_state.activity = []

if "selected_url" not in st.session_state:
    st.session_state.selected_url = ""


# =========================================================
# HEADER
# =========================================================

st.title("🕷️ Simple Web Scraper")

st.write(
    "Enter a website URL and scrape available book data "
    "using Selenium."
)


# =========================================================
# SIDEBAR - HISTORY
# =========================================================

with st.sidebar:

    st.header("📜 Scraping History")

    history = load_history()

    if not history:

        st.info("No scraping history yet.")

    else:

        for index, item in enumerate(history):

            col1, col2 = st.columns([5, 1])

            with col1:

                if st.button(
                    item["url"],
                    key=f"history_{index}",
                    use_container_width=True
                ):

                    st.session_state.selected_url = item["url"]

                    st.rerun()

            with col2:

                if st.button(
                    "✕",
                    key=f"delete_{index}"
                ):

                    delete_history(index)

                    st.rerun()

            st.caption(item["time"])


# =========================================================
# URL INPUT
# =========================================================

url = st.text_input(
    "🌐 Website URL",
    value=st.session_state.selected_url,
    placeholder="https://books.toscrape.com/"
)


# =========================================================
# SUGGESTED WEBSITES
# =========================================================

st.subheader("🌐 Suggested Websites")

suggestions = {
    "📚 Books to Scrape": "https://books.toscrape.com/",
    "📚 Books - Page 2": "https://books.toscrape.com/catalogue/page-2.html",
    "📚 Books - Page 3": "https://books.toscrape.com/catalogue/page-3.html"
}


suggestion_columns = st.columns(len(suggestions))


for column, (name, website) in zip(
    suggestion_columns,
    suggestions.items()
):

    with column:

        if st.button(
            name,
            use_container_width=True
        ):

            st.session_state.selected_url = website

            st.rerun()


# =========================================================
# SCRAPE BUTTON
# =========================================================

st.write("")

scrape_button = st.button(
    "🔍 Scrape Website",
    type="primary",
    use_container_width=True
)


# =========================================================
# SCRAPING PROCESS
# =========================================================

if scrape_button:

    if not url.strip():

        st.error(
            "Please enter a website URL first."
        )

    else:

        # Clear previous data and activity
        st.session_state.scraped_data = []
        st.session_state.activity = []

        try:

            # First activity
            st.session_state.activity.append(
                "🚀 Starting scraper..."
            )

            data = scrape_books(
                url,
                status_callback=lambda message:
                st.session_state.activity.append(message)
            )

            if data:

                st.session_state.scraped_data = data

                add_to_history(url)

                st.session_state.activity.append(
                    "✅ Scraping completed successfully!"
                )

                st.success(
                    f"Successfully scraped {len(data)} books."
                )

            else:

                st.session_state.activity.append(
                    "⚠️ No data found."
                )

                st.warning(
                    "No books were found on this website."
                )

        except Exception as error:

            st.session_state.activity.append(
                "❌ An error occurred."
            )

            st.error(
                f"Scraping failed: {error}"
            )


# =========================================================
# ACTIVITY
# =========================================================

if st.session_state.activity:

    st.subheader("🔄 Activity")

    for activity in st.session_state.activity:

        st.write(activity)


# =========================================================
# RESULTS
# =========================================================

if st.session_state.scraped_data:

    st.subheader("📊 Scraped Results")

    dataframe = pd.DataFrame(
        st.session_state.scraped_data
    )

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True
    )


    # =====================================================
    # SAVE + CLEAR BUTTONS
    # =====================================================

    col1, col2 = st.columns(2)


    # =====================================================
    # SAVE DATA
    # =====================================================

    with col1:

        csv_data = dataframe.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="💾 Save Data",
            data=csv_data,
            file_name="scraped_data.csv",
            mime="text/csv",
            use_container_width=True
        )


    # =====================================================
    # CLEAR RESULTS
    # =====================================================

    with col2:

        if st.button(
            "🗑️ Clear Results",
            use_container_width=True
        ):

            st.session_state.scraped_data = []

            st.rerun()