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
        return 10 * (self.weight * .453592) + 6.25 * (self.height * 2.54) - 5 * self.age + 5 - ((self.temperature - 32) * (5 / 9)) * 10
