import requests
from bs4 import BeautifulSoup as bs

url = "https://weather.gc.ca/forecast/canada/index_e.html?id="

# hardcoding these because I want to do as little HTML scraping as possible, for efficiency reasons
# can't track when new cities appear in other provinces but i can easily hear about when new provinces appear

provinces = {
    "Alberta": {"ID": "AB", "Capital": "Edmonton"},
    "British Columbia": {"ID": "BC", "Capital": "Vancouver"},
    "Manitoba": {"ID": "MB", "Capital": "Winnipeg"},
    "New Brunswick": {"ID": "NB", "Capital": "Fredericton"},
    "Newfoundland": {"ID": "NL", "Capital": "St. John's"},
    "Northwest Territories": {"ID": "NT", "Capital": "Yellowknife"},
    "Nova Scotia": {"ID": "NS", "Capital": "Halifax"},
    "Nunavut": {"ID": "NU", "Capital": "Iqaluit"},
    "Ontario": {"ID": "ON", "Capital": "Ottawa (Richmond - Metcalfe)"},
    "Prince Edward Island": {"ID": "PE", "Capital": "Charlottetown"},
    "Quebec": {"ID": "QC", "Capital": "Quebec City"},
    "Saskatchewan": {"ID": "SK", "Capital": "Regina"},
    "Yukon": {"ID": "YT", "Capital": "Whitehorse"},
}

cities = (
    {}
)  # main functions writes to this list each time the bot starts up, can be refreshed tho


def get_search_data():
    for province in provinces.items():
        cities[province[1]["ID"]] = {}
        page = requests.get(url + province[1]["ID"])
        soup = bs(page.content, "html.parser")

        selected = soup.select("div.hidden-xs > div:nth-child(2) > div:nth-child(1)")

        for table in selected[0]:
            for link in table:
                if link != "\n":
                    to_add = {
                        link.text.lower(): (
                            str(
                                "https://weather.gc.ca"
                                + link.findChildren("a")[0].get("href")
                            )
                        )
                    }
                    cities[province[1]["ID"]].update(to_add)


def refresh():
    global cities
    cities.clear()
    get_search_data()
