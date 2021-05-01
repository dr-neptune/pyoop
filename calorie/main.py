from temperature import Temperature
from calorie import Calorie

temp = Temperature("usa", "worcester")
calories = Calorie(160, 68, 29, temp.get())

print(round(calories.calculate()))
