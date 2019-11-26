import requests
from bs4 import BeautifulSoup as bs
from settings import WEATHER_URL

URL = WEATHER_URL
page = requests.get(URL)
soup = bs(page.content, "html.parser")

# date
date_select = soup.select("dl.mrgn-bttm-0 > dd:nth-child(4)")[0]
date = date_select.text

# get image contents
img_select = soup.select(
    "details.hidden-xs > div:nth-child(3) > div:nth-child(1) > img:nth-child(1)"
)[0]
img = "https://weather.gc.ca" + img_select["src"]

# condition
condition_select = soup.select(
    "div.col-sm-4:nth-child(1) > dl:nth-child(1) > dd:nth-child(2)"
)[0]
condition = condition_select.text

# pressure
pressure_select = soup.select(
    "div.col-sm-4:nth-child(1) > dl:nth-child(1) > dd:nth-child(4)"
)[0]
pressure = pressure_select.text

# tendency
tendency_select = soup.select(
    "div.col-sm-4:nth-child(1) > dl:nth-child(1) > dd:nth-child(7)"
)[0]
tendency = tendency_select.text

# temperature
temperature_select = soup.select(
    "div.brdr-rght-city:nth-child(2) > dl:nth-child(1) > dd:nth-child(2)"
)[0]
temperature = temperature_select.text

# dew point
dew_select = soup.select(
    "div.brdr-rght-city:nth-child(2) > dl:nth-child(1) > dd:nth-child(5)"
)[0]
dew = dew_select.text

# humidity
humidity_select = soup.select(
    "div.brdr-rght-city:nth-child(2) > dl:nth-child(1) > dd:nth-child(8)"
)[0]
humidity = humidity_select.text

# wind
wind_select = soup.select(
    "div.col-sm-4:nth-child(3) > dl:nth-child(1) > dd:nth-child(2)"
)[0]
wind = wind_select.text

# visibility
visibility_select = soup.select(
    "div.col-sm-4:nth-child(3) > dl:nth-child(1) > dd:nth-child(5)"
)[0]
visibility = visibility_select.text
