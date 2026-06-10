import json
import re
import requests
import os
from bs4 import BeautifulSoup

URLS = [
    "https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html",
    "https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-bucks.html",
    "https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-meals.html",
    "https://roonee.com/restaurants-near-the-university-of-texas-at-el-paso/",
    "https://www.utep.edu/student-affairs/foodpantry/faq/",
    "https://www.utep.edu/student-affairs/foodpantry/visit-us/",
    "https://www.utep.edu/student-affairs/foodpantry/visit-us/"
]

CHUNK_SIZE = 200
CHUNK_OVERLAP = 50
OUTPUT_FILE = "chunks.json"


def load_url(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(" ")
    return clean_text(text)


def clean_text(text):
    text = text.replace("&amp;", "&")
    text = text.replace("&nbsp;", " ")

    remove_phrases = [
        "Skip to main content",
        "MinerAlert",
        "Main Content",
        "UTEP Business Affairs",
        "Miner Gold Card Office"
    ]

    for phrase in remove_phrases:
        text = text.replace(phrase, " ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def chunk_text(text):
    chunks = []
    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


all_chunks = []

for url in URLS:
    print(f"Loading: {url}")
    text = load_url(url)
    chunks = chunk_text(text)

    for i, chunk in enumerate(chunks):
        all_chunks.append({
            "source": url,
            "chunk_id": i,
            "text": chunk
        })

RAW_DIR = "data"

for filename in os.listdir(RAW_DIR):
    if filename.endswith(".txt"):
        path = os.path.join(RAW_DIR, filename)
        print(f"Loading local file: {path}")

        with open(path, "r", encoding="utf-8") as file:
            text = clean_text(file.read())

        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "source": filename,
                "chunk_id": i,
                "text": chunk
            })

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(all_chunks, file, indent=2)

print(f"\nCreated {len(all_chunks)} chunks.")

print("\nSample chunks:")

for chunk in all_chunks[:5]:
    print("-" * 50)
    print("Source:", chunk["source"])
    print("Chunk ID:", chunk["chunk_id"])
    print(chunk["text"])