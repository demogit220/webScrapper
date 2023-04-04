# Web Scrapper
- Made using Beautiful Soup
- Intern Task

<br>

# What does it do?
- Scrapes [verge.com]('https://www.theverge.com/')
- Collects the data of articles headlines, link, author and date present on the front page.
- Save the results to a .csv file and sqlite3 database with id set to as primary key
- Testing the code for bugs using pytest

<br>

# How to run locally on your pc
`git clone https://github.com/demogit220/webScrapper.git`

`cd webScrapper`

`pip install -r requirements.txt`

`python main.py`
- creates a .csv file titled 'ddmmyyy_verge.csv'
- creates a .db file

<br>

# How to run tests
`pytest tests/`




    



