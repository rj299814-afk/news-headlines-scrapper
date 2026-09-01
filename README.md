# news-headlines-scrapper


This project is a simple web scraper that collects news headlines
from a public news website using Python.

## Technologies Used

- Python
- Requests
- BeautifulSoup

## How It Works

1. The program sends a GET request to the news website.
2. The HTML content is received using the Requests library.
3. BeautifulSoup parses the HTML.
4. The program finds headline elements using `<h2>` tags.
5. The extracted headlines are saved in `headlines.txt`.

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
