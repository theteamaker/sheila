import requests
from bs4 import BeautifulSoup as bs
from settings import WEATHER_URL

URL = WEATHER_URL

page = requests.get(URL)

soup = bs(page.content, "html.parser")

table = soup.table
table_rows = table.find_all("tr")

days = []

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text for i in td]
    if len(row) != 0:
        if row[0] != " Night":
            days.append(row)


class Weatherday:
    def __init__(self, dayinfo):
        self.info = dayinfo[1]
        self.unparsed_date = dayinfo[0]

    def date(self):
        if u"\xa0" in self.unparsed_date:
            date_dict = {}
            unformatted_date = self.unparsed_date.split(",")

            # Getting the calendar date correct, and returning it in its proper form.
            day = unformatted_date[1].replace(u"\xa0", u" ").split(" ")
            day.remove(day[0])  # remove some empty space at the beginning of the list

            month_replacements = {
                "Jan": "January",
                "Feb": "February",
                "Mar": "March",
                "Apr": "April",
                "May": "May",
                "Jun": "June",
                "Jul": "July",
                "Aug": "August",
                "Sep": "September",
                "Oct": "October",
                "Nov": "November",
                "Dec": "December",
            }

            num_replacements = {
                "1": "st",
                "2": "nd",
                "3": "rd",
                "4": "th",
                "5": "th",
                "6": "th",
                "7": "th",
                "8": "th",
                "9": "th",
                "0": "th",
            }

            weekday_replacements = {
                "Mon": "Monday",
                "Tue": "Tuesday",
                "Wed": "Wednesday",
                "Thu": "Thursday",
                "Fri": "Friday",
                "Sat": "Saturday",
                "Sun": "Sunday",
            }

            for (
                month
            ) in (
                month_replacements.items()
            ):  # returning the month as a full name instead of abbr.
                if day[1] == month[0]:
                    date_dict["month"] = month[1]
                    break

            for num in num_replacements.items():
                if day[0].endswith(num[0]):
                    to_add = day[0] + num[1]
                    date_dict["day"] = to_add
                    break

            for weekday in weekday_replacements.items():
                if unformatted_date[0] == weekday[0]:
                    date_dict["weekday"] = weekday[1]

            return str(
                "{}, {} {}".format(
                    date_dict["weekday"], date_dict["month"], date_dict["day"]
                )
            )
        else:
            return self.unparsed_date
