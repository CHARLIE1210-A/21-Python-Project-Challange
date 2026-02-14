import requests
from bs4 import BeautifulSoup
import csv
import logging

# ================= LOGGING =================
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ================= FETCH HTML =================
def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=10)
    #raise error for bad responses, error if status != 200
    response.raise_for_status() 
    return response.text

# ================= PARSE HTML =================
def parse_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.title.text.strip() if soup.title else "No Title"
    
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text(strip=True)
        
        links.append({
            "page_title": title,
            "link_text": text,
            "href": href
        })
        
        return title, links
    
# ================= SAVE TO CSV =================
def save_to_csv(filename, links):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["page_title", "link_text", "href"])
        writer.writeheader()
        writer.writerows(links)
        
# ================= MAIN =================
def main():
    url = input("Enter the URL of the webpage: ").strip()
    
    try:
        html = fetch_page(url)
        title, links = parse_links(html, url)
        
        logger.info(f"Fetched {len(links)} links from '{title}' page.")
        
        save_to_csv("scraped_links.csv", links)
        logger.info("Links saved to 'scraped_links.csv.")
        
    except Exception as e:
        logger.error(f"An error occured: {e}")

if __name__ == "__main__":
    main()