import datetime
import requests
from bs4 import BeautifulSoup
# TODO get  hours work for each month in year
date = datetime.datetime.now()
URL = 'https://kalendarz.livecity.pl/czas-pracy/{}'.format(date.year)
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

