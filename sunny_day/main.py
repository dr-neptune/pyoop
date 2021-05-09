from sunnyday2 import Weather
from pprint import pprint

api_key = "26631f0f41b95fb9f5ac0df9a8f43c92"

weather = Weather(apikey=api_key, city="Nairobi")

pprint(weather.next_12h_simplified())
