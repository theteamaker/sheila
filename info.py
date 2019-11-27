import requests
from bs4 import BeautifulSoup as bs


def dataer(url):
    page = requests.get(url)
    soup = bs(page.content, "html.parser")

    info = soup.select("div.brdr-tp:nth-child(2)")[0]

    dataer = {}

    for tables in info:
        for table in tables:
            if table != "\n":
                titles = table.findChildren("dt")
                infos = table.findChildren("dd")

                for info in infos:
                    if "wxo-city-hidden" in info["class"]:
                        infos.remove(info)

                for index in range(len(titles)):
                    title = titles[index].text.replace("\n", "")
                    info = infos[index].text.replace("\n", "")
                    dataer[title] = info

    return dataer
