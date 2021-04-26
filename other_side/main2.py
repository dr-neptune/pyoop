from folium import Map, Marker, Popup
from geo import Geopoint
from functools import reduce

# get lat and lon
# latitude, longitude = 40.4, -3.7

locations = [[41, -1],
             [40, 2],
             [39, 5],
             [42, 6]]

print(locations[0][0])

# folium map instance
my_map = Map(location = [38, 4])

# create a geopoint instance
# geopoint = Geopoint(latitude, longitude)

# add a popup to it
# popup_content = reduce(lambda x, y: x + y,
#                        map(lambda x: f"{x[0][-8:-6]}h: {round(x[1])}°F <img src='http://openweathermap.org/img/wn/{x[3]}@2x.png' width=35><hr style=\"margin:1px\">",
#                            geopoint.get_weather()))

for loc in locations:
    geopoint = Geopoint(loc[0], loc[1])
    popup_content = reduce(lambda x, y: x + y,
                       map(lambda x: f"{x[0][-8:-6]}h: {round(x[1])}°F <img src='http://openweathermap.org/img/wn/{x[3]}@2x.png' width=35><hr style=\"margin:1px\">",
                           geopoint.get_weather()))
    popup = Popup(popup_content, max_width = 400).add_to(geopoint)
    geopoint.add_to(my_map)

# popup = Popup(popup_content, max_width = 400)
# popup.add_to(geopoint)
# geopoint.add_to(my_map)

# save the Map instance to an html file
my_map.save('map.html')
