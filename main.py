import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd

# Constants
save_file_path = "data/quotes.csv"

if __name__ == "__main__":
    # DataFrame Input Object
    quote_data = {
        "Quote": [],
        "Author": [],
        "Tags": [],
    }

    print("Started Scraping Quotes")

    # Scrape Quotes
    for i in range(10):
        page_link = "https://quotes.toscrape.com/page/" + str(i + 1)
        
        # Get the page
        response = requests.get(page_link)

        # Check the status
        if response.status_code != 200:
            print("Can't access site")
            break
        
        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find Quotes
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes: 
            # Find Quote text
            quote_data["Quote"].append(quote.find("span", class_="text").text)

            # Find Quote Author
            quote_data["Author"].append(quote.find("small", class_="author").text)

            # Find Quote Tags
            tag_list = []
            tags = quote.find_all("a", class_="tag")
            for tag in tags:
                tag_list.append(tag.text)
            tag_str = ", ".join(tag_list)
            quote_data["Tags"].append(tag_str)
        
        print(f"Scraped page {i + 1}")

    print("Finished Scraping Quotes")

    # Create DataFrame
    df = pd.DataFrame(quote_data)
    df.to_csv(save_file_path, index=False)
       
