class Geopoint:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return [round(self.latitude, 0), round(self.longitude, 0)]
