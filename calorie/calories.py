class Calorie:
    """
    Represent amount of calories.
    BMR = 10 * weight + 6.25 * height - 5 * age + 5 - 10 * temperature
    """
    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        weight = (float(self.weight) * .453592)
        height = (float(self.height) * 2.54)
        age = float(self.age)
        temp = ((float(self.temperature) - 32) * (5 / 9))
        return (10 * weight) + (6.25 * height) - (5 * age) + 5 - (temp * 10)
