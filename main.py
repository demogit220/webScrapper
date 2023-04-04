from Scrapper.scarpper import WebScraper
from Scrapper.save import SaveTo as st

if __name__ == '__main__':
    
    url = 'https://www.theverge.com/'
    scraper = WebScraper(url)
    scraper.scrape()
    st.save_to_csv(scraper)
    st.save_to_sqlite(scraper)
