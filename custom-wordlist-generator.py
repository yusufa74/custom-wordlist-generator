import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
import time

visited = set()
unique_words = set()
base_domain = ''

def extract_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words.update(words)

def crawl(url, depth=2):
    global base_domain
    if depth == 0 or url in visited:
        return
    try:
        print(f"[+] Visiting: {url}")
        response = requests.get(url, timeout=10)
        visited.add(url)
        time.sleep(1)
    except:
        return

    if response.status_code != 200 or 'text/html' not in response.headers.get('Content-Type', ''):
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    extract_words(soup.get_text())

    for link in soup.find_all('a', href=True):
        new_url = urljoin(url, link['href'])
        if base_domain in urlparse(new_url).netloc:
            crawl(new_url, depth - 1)

if __name__ == '__main__':
    domain = input("Enter domain (e.g. example.com): ").strip()
    max_words = input("Enter maximum number of words you want (e.g. 2000): ").strip()

    try:
        max_words = int(max_words)
    except ValueError:
        print("Please enter a valid number.")
        exit(1)

    if not domain.startswith('http'):
        start_url = 'https://' + domain
    else:
        start_url = domain
    base_domain = urlparse(start_url).netloc

    print(f"\n[+] Crawling {start_url}...\nThis may take a few moments.")
    crawl(start_url, depth=2)

    final_words = sorted(unique_words)[:max_words]

    with open('wordlist', 'w', encoding='utf-8') as f:
        for word in final_words:
            f.write(f"{word}\n")

    print(f"\n[+] Done! Saved {len(final_words)} words to 'wordlist'.")
