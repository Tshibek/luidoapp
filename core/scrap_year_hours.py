import requests
from bs4 import BeautifulSoup
import datetime


def scrap_monthly_hours(month, year):
    url = 'https://kalendarz.livecity.pl/czas-pracy/{}'.format(year)
    request = requests.get(url)
    bs = BeautifulSoup(request.content, features="html.parser")
    hours = bs.find_all(attrs={"data-title": "godz. pracujące"})
    hour = hours[month - 1].text
    hour = int(hour)
    return hour
