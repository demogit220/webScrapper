import os
import sqlite3
from datetime import date
import re
from tests import WebScraper,SaveTo
import csv

# Test Cases    
def test_articles_not_empty(scraper):
    assert len(scraper.articles) > 0

    for article in scraper.articles:
        assert (article[0]) != None 
        assert (article[1]) != None
        assert (article[2]) != None
        assert (article[3]) != None
        
        assert (article[0], str) != None
        assert (article[1], str) != None
        assert (article[2], str) != None
        assert (article[3], str) != None

    scraper = None

def test_article_contents_are_unique(scraper):
    article_set = set()
    for article in scraper.articles:
        assert article not in article_set
        article_set.add(article)

def test_article_date_format(scraper):
    for article in scraper.articles:
        assert re.match("^[A-Za-z]{3,9}, [0-9]{1,2} [A-Za-z]{3,9} [0-9]{4} at [0-9]{1,2}:[0-9]{2} (AM|PM)$", article[3]) is not None

def test_save_to_csv():
    save_to = SaveTo()
    # adding dummy data to articles attribute
    save_to.articles = [('https://www.example.com', 'Example Headline', 'John Doe', '2023-04-03')]
    # call save_to_csv method
    save_to.save_to_csv()
    # check if file exists and has correct name
    today = date.today().strftime('%d%m%Y')
    filename = f'{today}_verge.csv'
    assert os.path.isfile(filename)
    # check if file has correct header
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        assert next(reader) == ['URL', 'headline', 'author', 'date']
    # remove test file
    os.remove(filename)

def test_save_to_sqlite_primary_key(scraper):
    # Save articles to SQLite database
    saver = SaveTo()
    saver.articles = scraper.articles
    saver.save_to_sqlite()
    
    # Connect to database and get schema information
    conn = sqlite3.connect('verge_articles.db')
    c = conn.cursor()
    c.execute("PRAGMA table_info(articles)")
    table_info = c.fetchall()
    conn.close()
    
    # Check if id column is primary key
    id_col_info = table_info[0]
    assert id_col_info[0] == 0 # id column index
    assert id_col_info[2] == 'INTEGER'
    assert id_col_info[3] == 0 # primary key flag

    os.remove('verge_articles.db')
    

        