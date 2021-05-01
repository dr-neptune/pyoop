import requests
from pprint import pprint
from selectorlib import Extractor

headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

r = requests.get("https://www.timeanddate.com/weather/italy/rome", headers=headers)
content = r.text
extractor = Extractor.from_yaml_file("temperature.yaml")

raw_result = extractor.extract(content)["temp"].replace("\xa0°F", "")

print(raw_result)
