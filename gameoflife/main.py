import time

import numpy as np
import pygame

CELL_SIZE = 10
NUM_ROWS = 100
NUM_COLS = 150
SCREEN_HEIGHT = CELL_SIZE * NUM_ROWS
SCREEN_WIDTH = CELL_SIZE * NUM_COLS
DEAD_CELL = (36, 3, 70)
NEW_CELL = (160, 219, 142)
DYING_CELL = (60, 60, 60)
# DYING_CELL = (57, 28, 88)
LIVING_CELL = (255, 255, 255)


def init_surface():
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Nathan's game of life")
    surface.fill(DEAD_CELL)
    return surface


def user_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def init_cells():
    cells = np.random.randint(0, 2, (NUM_ROWS, NUM_COLS))
    return cells


def cell_lives_next_generation(cells, row, col):
    num_neighbors = (
        np.sum(cells[row - 1 : row + 2, col - 1 : col + 2]) - cells[row, col]
    )

    if cells[row, col] == 1:
        return num_neighbors == 2 or num_neighbors == 3
    else:
        return num_neighbors == 3


def calculate_next_generation(cells):
    next_generation = np.zeros(cells.shape)
    for row, col in np.ndindex(cells.shape):
        next_generation[row, col] = (
            1 if cell_lives_next_generation(cells, row, col) else 0
        )
    return next_generation


def get_cell_color(prev_cell, next_cell):
    if prev_cell == 1:
        if next_cell == 1:
            return LIVING_CELL
        else:
            return DYING_CELL
    else:
        if next_cell == 1:
            return NEW_CELL
        else:
            return DEAD_CELL


def draw_updates(prev_gen, next_gen, surface):
    for row, col in np.ndindex(prev_gen.shape):
        rectangle = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
        color = get_cell_color(prev_gen[row, col], next_gen[row, col])
        pygame.draw.rect(surface, color, rectangle)


def main():
    cells = init_cells()
    surface = init_surface()
    draw_updates(np.zeros(cells.shape), cells, surface)
    pygame.display.update()
    while True:
        if user_quit():
            pygame.quit()
            return
        time.sleep(0.25)
        next_generation = calculate_next_generation(cells)
        draw_updates(cells, next_generation, surface)
        pygame.display.update()
        cells = next_generation


if __name__ == "__main__":
    pygame.init()
    main()
