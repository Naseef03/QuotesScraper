import requests
import os
from bs4 import BeautifulSoup
import pandas as pd

# Constants
BASE_URL = "https://quotes.toscrape.com"
OUTPUT_DIR = "data"
CSV_FILE = os.path.join(OUTPUT_DIR, "quotes.csv")

def fetch_page(url):
    """
    Fetch the page content given the url
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_quotes(html):
    """
    Extract the quotes from the html
    """
    soup = BeautifulSoup(html, "html.parser")
    quotes_data = []

    # Find Quotes
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes: 
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]

        quotes_data.append({"text": text, "author": author, "tags": tags})

    return quotes_data


def scrape_all_quotes():
    """
    Scrape quotes from every page in the BASE_URL
    """
    all_quotes = []
    page_url = "/page/1"

    while page_url:
        print(f"Scraping {BASE_URL + page_url}")

        # Scrape the page
        html = fetch_page(BASE_URL + page_url)
        quotes = extract_quotes(html)
        all_quotes.extend(quotes)

        # Find next page
        soup = BeautifulSoup(html, "html.parser")
        next_page = soup.find("li", class_="next")
        page_url = next_page.find("a").get("href") if next_page else None

    return all_quotes


def save_quotes(quotes, file_path):
    """
    Save given Quotes to the given file_path
    """
    df = pd.DataFrame(quotes)
    df.to_csv(file_path, index=False)



if __name__ == "__main__":
    quotes = scrape_all_quotes()
    save_quotes(quotes, CSV_FILE)   
