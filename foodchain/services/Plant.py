from .LifeForm import LifeForm


class Plant(LifeForm):
    def __init__(self, x, y, energy=100, color=(10, 89, 67)):
        super().__init__(x, y, energy, color)
        self.eaten = False
        self.family = "Plant"

    def tick(self):
        if self.energy < 1000 and not self.eaten:
            self.energy += 1

    def eat(self):
        self.eaten = True
