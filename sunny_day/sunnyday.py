import requests


class Weather:
    """
    Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates.

    Package use example:

    # given city
    weather = Weather(apikey=api_key, city="Boston")

    # given lat and lon
    weather = Weather(apikey=api_key, lat=4.1, lon=4.5)

    # get next 12h
    weather.next_12h()

    # get next 12h simplified
    weather.next_12h_simplified()
    """

    def __init__(self, apikey, city=None, lat=None, lon=None, units="imperial"):
        if city and (lat or lon):
            raise TypeError("Please choose either a city OR lat and lon arguments.")
        elif city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units={units}"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units={units}"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Please choose either a city or lat and lon arguments.")

        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        """
        Returns 3-hour data for the next 12 hours as a dict
        """
        return self.data["list"][:4]

    def next_12h_simplified(self, num_items=4):
        """
        Returns a tuple containing:
        (time period, temperature (F), feels like (F), weather description)
        """
        return [
            (
                i["dt_txt"],
                i["main"]["temp"],
                i["main"]["feels_like"],
                i["weather"][0]["description"],
            )
            for i in self.data["list"][:num_items]
        ]
