from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

URL = "https://utepdining.sodexomyway.com/en-us/locations/"

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # set True later
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)

    html = page.content()
    browser.close()

soup = BeautifulSoup(html, "html.parser")

for tag in soup(["script", "style", "nav", "footer", "header"]):
    tag.decompose()

text = clean_text(soup.get_text(" "))

print(text)

with open("utep_dining_locations.txt", "w", encoding="utf-8") as file:
    file.write(text)