import math


class LifeForm:
    def __init__(self, x, y, energy, color):
        self.x = x
        self.y = y
        self.energy = energy
        self.color = color

    def get_radius(self):
        self.energy = self.energy if self.energy > 0 else 0
        return math.sqrt(self.energy / math.pi)

    def tick(self):
        raise Exception("tick not implemented")
