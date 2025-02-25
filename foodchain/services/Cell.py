import math
import random
import string

from .LifeForm import LifeForm


class Cell(LifeForm):
    def __init__(
            self,
            x,
            y,
            direction,
            family,
            eats_plants=True,
            eats_animals=False,
            field_of_view=math.pi / 2,
            depth_of_view=500,
            energy=1000,
            metabolism_energy=1,
            eat_efficiency=.5,
            reproduce_efficiency=.8,
            reproduce_threshold=2000,
            mutation_rate=.5,
            mutation_magnitude=.2,
            color=(144, 97, 41),
            allow_carnivore_mutation=False,
            allow_herbivore_mutation=False
        ):
        super().__init__(x, y, energy, color)

        self.id = ''.join([
            random.choice(string.ascii_lowercase)
            for _
            in range(32)
        ])
        self.family=family

        self.dead = False

        self._set_direction(direction)
        self.field_of_view = min(2 * math.pi, max(0, field_of_view))
        self.depth_of_view = depth_of_view if depth_of_view > 0 else 0

        self.metabolism_energy = metabolism_energy
        self.eat_efficiency = eat_efficiency
        self.reproduce_efficiency = reproduce_efficiency
        self.reproduce_threshold = reproduce_threshold
        self.mutation_rate = mutation_rate
        self.mutation_magnitude = mutation_magnitude
        self.eats_plants = eats_plants
        self.eats_animals = eats_animals
        self.allow_carnivore_mutation=allow_carnivore_mutation
        self.allow_herbivore_mutation=allow_herbivore_mutation

    def __str__(self):
        return f"x: {round(self.x)}, y: {round(self.y)}, e: {round(self.energy)}"

    def _get_movement(self, stand_still=False):
        max_velocity = 5 if not self.eats_animals else 10
        velocity = 0 if stand_still or self.energy == 0 else 5000 / (self.energy)
        if velocity > max_velocity:
            velocity = max_velocity
        energy_expense = .2 * velocity ** (.5) * self.energy ** (1.0 / 4.0)
        energy_expense += self.metabolism_energy
        return velocity, energy_expense

    def _set_direction(self, val):
        self.direction = self._adjust_radians(val)

    @staticmethod
    def _adjust_radians(val):
        if val < -1 * math.pi:
            return val + 2 * math.pi
        elif val > math.pi:
            return val - 2 * math.pi
        else:
            return val

    def _move(self, stand_still=False):
        velocity, energy_expense = self._get_movement(stand_still=stand_still)

        # Move
        vel_x = math.cos(self.direction) * velocity
        vel_y = math.sin(self.direction) * velocity
        self.x += vel_x
        self.y += vel_y

        # Use Energy
        self.energy -= energy_expense
        if self.energy <= 0:
            self.energy = 0

    def tick(self, plants, cells):
        if self.energy <= 0:
            self.dead = True

        food = []
        if self.eats_plants:
            food.extend(plants)
        if self.eats_animals:
            food.extend(cells)
        target_food = self._find_food(food)

        if not target_food:
            self._set_direction(self.direction + self.field_of_view)
        else:
            self._set_direction(self._target_bearing(target_food.x, target_food.y))
            if self._target_range(target_food.x, target_food.y) < self.get_radius() + target_food.get_radius():
                # We're super close, eat that plant
                self._eat_plant(target_food)

        stand_still = not target_food
        self._move(stand_still=stand_still)
        return self._reproduce()

    def _target_bearing(self, x, y):
        return self._adjust_radians(math.atan2(y - self.y, x - self.x))

    def _target_range(self, x, y):
        try:
            return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        except:
            raise Exception(f"id: {self.id}, self.x: {self.x}, x: {x}, self.y: {self.y}, y: {y}")

    def _calculate_fov(self):
        fov_left = self._adjust_radians(self.direction + self.field_of_view * .5)
        fov_right = self._adjust_radians(fov_left - self.field_of_view)
        return fov_left, fov_right

    def _target_in_fov(self, x, y):
        fov_left, fov_right = self._calculate_fov()
        direction_to_target = self._target_bearing(x, y)
        right_of_left_fov = direction_to_target < fov_left
        left_of_right_fov = direction_to_target > fov_right

        # If the cell is looking left, fov_left << fov_right
        if fov_left < fov_right:
            if direction_to_target > 0:
                # Target is right of center, i.e. positive
                return left_of_right_fov
            elif direction_to_target < 0:
                # Target is left of center, i.e. negative
                return right_of_left_fov
            else:
                return True
        else:
            return right_of_left_fov and left_of_right_fov

    def _target_in_range(self, x, y):
        return self._target_range(x, y) <= self.depth_of_view

    def _can_see(self, x, y):
        return self._target_in_range(x, y) and self._target_in_fov(x, y)

    def _find_food(self, food):
        food_can_see = [
            {"food": f, "range": self._target_range(f.x, f.y)}
            for f
            in food
            if self._can_see(f.x, f.y) and self.family != f.family
        ]

        if not food_can_see:
            return False

        closest_range = min([x['range'] for x in food_can_see])
        return [x['food'] for x in food_can_see if x['range'] == closest_range][0]

    def _eat_plant(self, plant):
        plant.eat()
        self.energy += self.eat_efficiency * plant.energy

    def _mutate(self, val, max_val=None, min_val=None, force_mutate=False):
        will_mutate = random.random() < self.mutation_rate
        if not will_mutate and not force_mutate:
            return val
        mutate_magnitude = self.mutation_magnitude * (2 * random.random() - 1)
        new_val = val * (1 + mutate_magnitude)
        new_val = min(max_val, new_val) if max_val is not None else new_val
        new_val = max(min_val, new_val) if min_val is not None else new_val
        return new_val

    def _reproduce(self):
        if self.energy < self.reproduce_threshold:
            return False
        self.energy = .5 * self.energy

        r = self._mutate(self.color[0], force_mutate=True, min_val=0, max_val=255)
        g = self._mutate(self.color[1], force_mutate=True, min_val=0, max_val=255)
        b = self._mutate(self.color[2], force_mutate=True, min_val=0, max_val=255)
        new_color = (r, g, b)

        child = Cell(
            self.x,
            self.y,
            self.direction,
            self.family,
            field_of_view=self._mutate(self.field_of_view, max_val=math.pi * 2, min_val=0),
            depth_of_view=self._mutate(self.depth_of_view, min_val=0),
            energy=self.energy * self.reproduce_efficiency,
            metabolism_energy=self._mutate(self.metabolism_energy, min_val=0),
            eat_efficiency=self._mutate(self.eat_efficiency, min_val=0, max_val=1),
            reproduce_efficiency=self._mutate(self.reproduce_efficiency, min_val=0, max_val=1),
            reproduce_threshold=self._mutate(self.reproduce_threshold, min_val=1),
            mutation_rate=self._mutate(self.mutation_rate, min_val=0, max_val=1),
            mutation_magnitude=self._mutate(self.mutation_magnitude, min_val=0),
            eats_animals=self.eats_animals,
            eats_plants=self.eats_plants,
            color=new_color,
        )
        distance = self.get_radius() + child.get_radius()
        direction = random.random() * 2 * math.pi
        child._set_direction(direction)
        x = math.cos(direction) * distance + self.x
        y = math.sin(direction) * distance + self.y
        child.x = x
        child.y = y

        if self.allow_herbivore_mutation and random.random() < self.mutation_rate:
            child.eats_plants = not self.eats_plants
        if self.allow_carnivore_mutation and random.random() < self.mutation_rate:
            child.eats_animals = not self.eats_animals

        return child

    def eat(self):
        self.dead = True
