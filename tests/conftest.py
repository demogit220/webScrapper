import pytest
from tests import WebScraper,SaveTo

@pytest.fixture
def scraper():
    url = 'https://www.theverge.com/'
    scraper = WebScraper(url)
    scraper.scrape()
    return scraper

