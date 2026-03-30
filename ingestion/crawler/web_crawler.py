import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

def crawl_website(start_url, max_pages=15):
    visited = set()
    queue = deque([start_url])
    results = []

    domain = urlparse(start_url).netloc

    while queue and len(visited) < max_pages:
        url = queue.popleft()

        if url in visited:
            continue

        try:
            res = requests.get(url, timeout=5)
            if res.status_code != 200:
                continue

            soup = BeautifulSoup(res.text, "html.parser")
            text = soup.get_text(" ", strip=True)

            results.append((url, text))
            visited.add(url)

            for link in soup.find_all("a", href=True):
                next_url = urljoin(url, link["href"])
                if urlparse(next_url).netloc == domain:
                    queue.append(next_url)

        except:
            continue

    return results