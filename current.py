import requests
from bs4 import BeautifulSoup as bs
from settings import WEATHER_URL

class Current:
    def __init__(self, url):
        page = requests.get(url)
        soup = bs(page.content, "html.parser")

        # date
        self.date = soup.select(
            "dl.mrgn-bttm-0 > dd:nth-child(4)"
            )[0].text

        #condition
        self.condition = soup.select(
            "div.col-sm-4:nth-child(1) > dl:nth-child(1) > dd:nth-child(2)"
        )[0].text

        # pressure
        self.pressure = soup.select(
            "div.col-sm-4:nth-child(1) > dl:nth-child(1) > dd:nth-child(4)"
        )[0].text

        # tendency
        self.tendency = soup.select(
            "div.col-sm-4:nth-child(1) > dl:nth-child(1) > dd:nth-child(7)"
        )[0].text

        # temperature
        self.temperature = soup.select(
            "div.brdr-rght-city:nth-child(2) > dl:nth-child(1) > dd:nth-child(2)"
        )[0].text

        # dew point
        self.dew = soup.select(
            "div.brdr-rght-city:nth-child(2) > dl:nth-child(1) > dd:nth-child(5)"
        )[0].text

        # humidity
        self.humidity = soup.select(
            "div.brdr-rght-city:nth-child(2) > dl:nth-child(1) > dd:nth-child(8)"
        )[0].text

        # wind
        self.wind = soup.select(
            "div.col-sm-4:nth-child(3) > dl:nth-child(1) > dd:nth-child(2)"
        )[0].text

        # visibility
        self.visibility = soup.select(
            "div.col-sm-4:nth-child(3) > dl:nth-child(1) > dd:nth-child(5)"
        )[0].text

        # get image contents
        self.image = "https://weather.gc.ca" + soup.select(
            "details.hidden-xs > div:nth-child(3) > div:nth-child(1) > img:nth-child(1)"
        )[0]["src"]