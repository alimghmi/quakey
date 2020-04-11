import re
from bs4 import BeautifulSoup
from urllib.request import urlopen as requests


class Equake(object):

    def __init__(self):
        self.url = "http://irsc.ut.ac.ir/"
        self.content = None
        
    def request(self):
        try:
            r = requests(self.url)
        except Exception as e:
            print(e)
            exit()

        return r

    def soup(self):
        return BeautifulSoup(self.request().read(), 'html.parser')

    def graber(self):
        soup = self.soup()

        rows = soup.find_all('tr', class_="DataRow1") + \
            soup.find_all('tr', class_="DataRow2")

        return rows

    def parser(self, row):
        content = row.find_all('td')

        location = re.match("(.*),(.*)", content[5].text
                            .encode('ascii', 'ignore')
                            .decode().replace(" ", "").lower())

        data = {

            "date": content[0].text.
            replace("   ", "").replace("  ", ""),

            "magnitude": float(content[1].text),
            "lat": float(content[2].text),
            "lon": float(content[3].text),
            "depth": float(content[4].text),
            "zone": location[1],
            "province": location[2],
            "url": content[0].find("a")['href']

        }

        return data

    def miner(self):
        rows = self.graber()
        if len(rows) != 0:
            result = list()
            for row in rows:
                result.append(self.parser(row))

            self.content = result
            return
        return False

    def largevn(self):
        return [ x for x in self.content if x['magnitude'] >= 3.0 ]

    def geoflt(self, geo):
        if not isinstance(geo, str):
            return False

        return [ x for x in self.content if geo.lower() \
            in (x['zone'], x['province']) ]
