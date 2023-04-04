import requests
from bs4 import BeautifulSoup
from dateutil import parser
import json

class WebScraper:
    
    def __init__(self, url):
        self.url = url
        self.articles = []
    
    def scrape(self):
        # Make request to website
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all article links
        article_links = soup.find_all("script")
        data = json.loads(article_links[24].text)
        
        articles_list = data['props']['pageProps']['hydration']['responses'][0]['data']['community']['frontPage']['placements']
        index = 0
        
        for ind in articles_list:
            if(ind['placeable']== None or ind['placeable']['title'] == None):
                continue
            headline = ind['placeable']['title']
            author = ind['placeable']['author']['fullOrUserName']
            link = ind['placeable']['url']
            Date = ind['placeable']['publishDate']
            date_obj = parser.parse(Date).strftime("%A, %d %B %Y at %I:%M %p")

            self.articles.append((headline,author,link,date_obj))
            index+=1