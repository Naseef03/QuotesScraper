import requests
import sys
from bs4 import BeautifulSoup

page_link = "https://quotes.toscrape.com"

if __name__ == "__main__":
    # Get the page
    response = requests.get(page_link)

    # Check the status
    if response.status_code != 200:
        print("Can't access site")
        sys.exit()
    
    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find Quotes
    quotes = soup.find_all("div", class_="quote", limit=100)


    count = 1
    for quote in quotes: 
        # Find Quote text
        text = quote.find("span", class_="text")
        print("Text:", text.text)

        # Find Quote Author
        author = quote.find("small", class_="author")
        print("Author:", author.text)

        # Find Quote Tags
        tag_list = []
        tags = quote.find_all("a", class_="tag")
        for tag in tags:
            tag_list.append(tag.text)
        tag_str = ", ".join(tag_list)
        print("Tags:", tag_str)

        print(count)
        count += 1

        print()
        print("="*20)
        print()
        

