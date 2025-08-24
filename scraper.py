import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_headlines():
    url = "https://www.bbc.com/news"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve webpage")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Find headline elements (BBC uses <h3> tags with 'gs-c-promo-heading__title')
    headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")

    # Save results to CSV
    filename = f"headlines_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])  # Header
        for h in headlines:
            writer.writerow([h.get_text(strip=True)])

    print(f"Scraped {len(headlines)} headlines and saved to {filename}")


if __name__ == "__main__":
    scrape_headlines()
