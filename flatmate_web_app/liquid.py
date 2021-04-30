class Matter:
    def __init__(self, temperature, freezing, boiling):
        self.boiling = boiling
        self.freezing = freezing
        self.temperature = temperature

    def state(self):
        if self.temperature < self.freezing:
            return "solid"
        elif self.temperature > self.boiling:
            return "gas"
        else:
            return "liquid"


class Water(Matter):
    def __init__(self, temperature):
        super().__init__(temperature, 0, 100)


class Mercury(Matter):
    def __init__(self, temperature):
        super().__init__(temperature, -38.83, 356.7)

worder = Water(99)
print(worder.state())
mercury_inst = Mercury(410)
print(mercury_inst.state())

# alternatively
# Ardit Solution:
class Matter:
    boiling_temperature = None
    freezing_temperature = None

    def __init__(self, temperature):
        self.temperature = temperature

    def state(self):
        if self.temperature <= self.freezing_temperature:
            return "solid"
        elif self.temperature >= self.boiling_temperature:
            return "gas"
        else:
            return "liquid"


class Water(Matter):
    boiling_temperature = 100
    freezing_temperature = 0


class Mercury(Matter):
    boiling_temperature = 356.7
    freezing_temperature = -38.83
