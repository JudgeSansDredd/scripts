import math
import random
import string
from random import randint

import pygame
from services.Cell import Cell
from services.Plant import Plant
from services.PygameService import PygameService

SCREEN_WIDTH=1900
SCREEN_HEIGHT=1080
SCREEN_SCALE=.8
MAX_PLANTS=100
STARTING_NUM_CELLS=10
HEIGHT = SCREEN_HEIGHT * SCREEN_SCALE
WIDTH = SCREEN_WIDTH * SCREEN_SCALE
INCLUDE_CARNIVORE=True
INCLUDE_OMNIVORE=False
ALLOW_CARNIVORE_MUTATION=False
ALLOW_HERBIVORE_MUTATION=False

def update_plants(plants):
    if len(plants) < MAX_PLANTS:
        new_plant = Plant(randint(1, WIDTH), randint(1, HEIGHT))
        plants.append(new_plant)
    return [p for p in plants if not p.eaten]

def update_cells(cells):
    return [
        c
        for c
        in cells
        if not c.dead
        and c.x <= WIDTH
        and c.y <= HEIGHT
        and c.x > 0
        and c.y > 0
    ]

def game_tick(cells, plants):
    for p in plants:
        p.tick()
    for c in cells:
        new_cell = c.tick(plants, cells)
        if new_cell:
            cells.append(new_cell)
    return update_cells(cells), update_plants(plants)

def init_cells():
    cells = []
    if INCLUDE_CARNIVORE:
        cells.append(Cell(
            random.randint(1, WIDTH),
            random.randint(1, HEIGHT),
            random.random() * 2 * math.pi,
            ''.join([
                random.choice(string.ascii_lowercase)
                for _
                in range(32)
            ]),
            color=(255, 50, 50),
            eats_animals=True,
            eats_plants=False,
            metabolism_energy=8,
            allow_carnivore_mutation=ALLOW_CARNIVORE_MUTATION,
            allow_herbivore_mutation=ALLOW_HERBIVORE_MUTATION
        ))
    if INCLUDE_OMNIVORE:
        cells.append(Cell(
            random.randint(1, WIDTH),
            random.randint(1, HEIGHT),
            random.random() * 2 * math.pi,
            ''.join([
                random.choice(string.ascii_lowercase)
                for _
                in range(32)
            ]),
            color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            eats_animals=True,
            allow_carnivore_mutation=ALLOW_CARNIVORE_MUTATION,
            allow_herbivore_mutation=ALLOW_HERBIVORE_MUTATION
        ))
    herbivores = [
        Cell(
            random.randint(1, WIDTH),
            random.randint(1, HEIGHT),
            random.random() * 2 * math.pi,
            ''.join([
                random.choice(string.ascii_lowercase)
                for _
                in range(32)
            ]),
            color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            metabolism_energy=2,
            reproduce_threshold=1500,
            eat_efficiency=.9,
            allow_carnivore_mutation=ALLOW_CARNIVORE_MUTATION,
            allow_herbivore_mutation=ALLOW_HERBIVORE_MUTATION
        )
        for _
        in range(STARTING_NUM_CELLS - len(cells))
    ]
    cells.extend(herbivores)
    return cells

def main():
    drawing_service = PygameService(WIDTH, HEIGHT)
    cells = init_cells()
    plants = []

    while True:
        if drawing_service.check_user_quit():
            return
        cells, plants = game_tick(cells, plants)
        drawing_service.clear_screen()
        drawing_service.draw_cells(cells)
        drawing_service.draw_plant(plants)
        pygame.display.update()

if __name__ == '__main__':
    main()
