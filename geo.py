from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather

help(Weather)

weather2 = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = 41.1, lon = -4.1)

print(weather2.next_12h_simplified())

class Geopoint:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.weather_key = "26631f0f41b95fb9f5ac0df9a8f43c92"

    def closest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat = self.latitude, lng = self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now

    def get_weather(self):
        weather = Weather(apikey = self.weather_key, lat = self.latitude, lon = self.longitude)
        return weather.next_12h_simplified()


tokyo = Geopoint(latitude = 35.7, longitude = 139.7)
print(tokyo.closest_parallel())
print(tokyo.get_time())
print(tokyo.get_weather())
