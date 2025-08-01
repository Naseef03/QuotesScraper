import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd

# Constants
page_link = "https://quotes.toscrape.com"
quotes_limit = 100
save_file_path = "data/quotes.csv"

if __name__ == "__main__":
    # Get the page
    response = requests.get(page_link)

    # Check the status
    if response.status_code != 200:
        print("Can't access site")
        sys.exit()
    
    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # DataFrame Input Object
    quote_data = {
        "Text": [],
        "Author": [],
        "Tags": [],
    }

    # Find Quotes
    quotes = soup.find_all("div", class_="quote", limit=100)

    for quote in quotes: 
        # Find Quote text
        quote_data["Text"].append(quote.find("span", class_="text").text)

        # Find Quote Author
        quote_data["Author"].append(quote.find("small", class_="author").text)

        # Find Quote Tags
        tag_list = []
        tags = quote.find_all("a", class_="tag")
        for tag in tags:
            tag_list.append(tag.text)
        tag_str = ", ".join(tag_list)
        quote_data["Tags"].append(tag_str)

    # Create DataFrame
    df = pd.DataFrame(quote_data)
    print(df)
    df.to_csv(save_file_path, index=False)
       
