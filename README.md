# 🕷️ Simple Web Scraper

A simple web scraping application built using Python, Selenium, Streamlit, and Pandas.

This application allows users to enter a website URL, scrape book data, view the results in a user-friendly interface, and save the scraped data as a CSV file.

## 🌐 Live Demo

[Open Live Web Scraper](https://simple-web-scraper-moifiurzbyntcaxv7mwfgv.streamlit.app/)

## 📂 GitHub Repository

[View Source Code](https://github.com/shubham-maurya-30/simple-web-scraper)

## ✨ Features

- 🌐 Enter a website URL
- 📚 Suggested website for testing
- 🔍 Scrape book data using Selenium
- 📊 Display scraped data in a table
- 🔄 Show scraping activity
- 📜 Maintain scraping history
- ❌ Delete individual history entries
- 💾 Save scraped data as CSV
- 🗑️ Clear scraped results
- 📱 Works on desktop and mobile browsers

## 🛠️ Technologies Used

- Python
- Selenium
- Streamlit
- Pandas

## 📁 Project Structure

```text
simple-web-scraper/
│
├── app.py
├── scraper.py
├── requirements.txt
├── packages.txt
├── README.md
└── .gitignore



⚙️ How It Works
User enters a website URL.
Selenium opens the website.
The scraper searches for available book elements.
Book title and price are extracted.
The scraped data is displayed in the Streamlit interface.
The user can save the data as a CSV file.
The website is added to scraping history.
▶️ Run Locally

Clone the repository:

git clone https://github.com/shubham-maurya-30/simple-web-scraper.git

Open the project folder:

cd simple-web-scraper

Install the required Python packages:

pip install -r requirements.txt

Run the application:

streamlit run app.py
📊 Example Output

The scraper extracts information such as:

Title	Price
A Light in the Attic	£51.77
Tipping the Velvet	£53.74
Soumission	£50.10
🎯 Project Purpose

This project was created to practice:

Web scraping
Selenium browser automation
Python programming
Streamlit application development
Data handling with Pandas
Git and GitHub
Cloud deployment
🚀 Deployment

The application is deployed using Streamlit Community Cloud.

Launch the Live App

👨‍💻 Author

Shubham Maurya

GitHub Profile
