import requests
from bs4 import BeautifulSoup

# News website URL
url = "https://www.bbc.com/news"

# User-Agent makes the request look like it is coming from a normal browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    # Send GET request to the website
    response = requests.get(url, headers=headers, timeout=10)

    # Check whether the request was successful
    response.raise_for_status()

    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all h2 headline tags
    headlines = soup.find_all("h2")

    # Remove duplicate headlines
    unique_headlines = []

    for headline in headlines:
        title = headline.get_text(strip=True)

        if title and title not in unique_headlines:
            unique_headlines.append(title)

    # Save headlines to a text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, title in enumerate(unique_headlines, start=1):
            file.write(f"{i}. {title}\n")

    print("Headlines scraped successfully!")
    print(f"Total headlines found: {len(unique_headlines)}")
    print("Saved to headlines.txt")

except requests.exceptions.RequestException as error:
    print("Error while accessing the website:", error)