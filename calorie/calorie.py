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
        def lbs_to_kg(wt):
            return float(wt) * .453592

        def in_to_cm(ht):
            return float(ht) * 2.54

        def f_to_c(temp):
            return (float(temp) - 32) * (5/9)

        weight = lbs_to_kg(self.weight)
        height = in_to_cm(self.height)
        age = float(self.age)
        temp = f_to_c(self.temperature)
        return (10 * weight) + (6.25 * height) - (5 * age) + 5 - (temp * 10)
