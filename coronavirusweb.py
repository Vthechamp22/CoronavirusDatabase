# imports
import requests
import json
from bs4 import BeautifulSoup


# base url for the data
_url = 'https://www.worldometers.info/coronavirus/'


def check():

    _update = dict()
    data = list()
    locations = list()
    req = requests.get(_url).content
    soup = BeautifulSoup(req, 'html.parser')
    rows = soup.find_all('tr')

    for row in rows[0:-8]:
        cols = row.find_all('td')
        for col in cols:
            if col.find('a') is not None:
                locations.append(col.find('a').text)
            data.append(col.text)

    country_data = data[104]
    print(country_data)
    for loc in locations:
        _update.update({
            loc: {
                "TC": country_data[country_data.index(loc) + 1],
                "NC": country_data[country_data.index(loc) + 2],
                "TD": country_data[country_data.index(loc) + 3],
                "ND": country_data[country_data.index(loc) + 4],
                "TR": country_data[country_data.index(loc) + 5],
                "AC": country_data[country_data.index(loc) + 6],
                "SC": country_data[country_data.index(loc) + 7],
                "TCpM": country_data[country_data.index(loc) + 8],
                "DpM": country_data[country_data.index(loc) + 9],
                "TT": country_data[country_data.index(loc) + 10],
                "TpM": country_data[country_data.index(loc) + 11],
            }
        })
    with open('worldwide.json', 'w') as f:
        json.dump(_update, f)


check()
