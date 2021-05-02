import requests
from selectorlib import Extractor


class Temperature:
    """
    Represent a temperature value extracted from
    the webpage: timeanddate.com/weather
    """
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    xpath_selector = """
    temp:
      xpath: '/html/body/div[6]/main/article/section[1]/div[1]/div[2]'
    """

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def get(self):
        # form url string
        url = f"https://www.timeanddate.com/weather/{self.country}/{self.city}"

        # get page text
        content = requests.get(url, headers=self.headers).text

        # instantiate the extractor object
        extractor = Extractor.from_yaml_string(self.xpath_selector)

        # return the extracted temperature as a single number
        return float(extractor.extract(content)["temp"]
                     .replace("\xa0°F", "")
                     .strip())
