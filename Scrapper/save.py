import pandas as pd
import sqlite3
from datetime import date

class SaveTo:

    def save_to_csv(self):
        # Save articles to CSV file
        today = date.today().strftime('%d%m%Y')
        filename = f'{today}_verge.csv'
        df = pd.DataFrame(self.articles, columns=['URL', 'headline', 'author', 'date'])
        df.to_csv(filename, index=False)
    
    def save_to_sqlite(self):
        # Save articles to SQLite database
        conn = sqlite3.connect('verge_articles.db')
        c = conn.cursor()
        # Create table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS articles
                     (id INTEGER PRIMARY KEY, URL TEXT, headline TEXT, author TEXT, date TEXT)''')
        # Insert articles into table
        for article in self.articles:
            c.execute('INSERT OR IGNORE INTO articles (URL, headline, author, date) VALUES (?, ?, ?, ?)', article)
        conn.commit()
        conn.close()