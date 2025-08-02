# Quotes Scraper

This project scrapes quotes from https://quotes.toscrape.com and stores them in a CSV file. Each quote 
includes text author and associated tags.

## Technologies used
- Python
- Requests
- BeautifulSoup
- Pandas

## Output
Data is saved in `data/quotes.csv` with the following columns
- Quote
- Author
- Tags

## How to Run
```bash
pip install -r requirements.txt
python main.py
```