
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class WebScraper:
    
    
    def __init__(self, url: str, lang: str = ""):
        self.url = url
        self.lang = lang.strip()
        self.soup = None


    def validate_url(self) -> bool:
        try:
            result = urlparse(self.url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False


    def fetch_page(self) -> bool:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }

            if self.lang:
                headers["Accept-Language"] = self.lang

            response = requests.get(self.url, headers=headers, timeout=10)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, 'html.parser')
            return True
        except requests.RequestException as e:
            print(f"[Erreur] Impossible d'accéder à la page: {e}")
            return False


    def get_soup(self) :
        return self.soup


    def get_url(self) :
        return self.url