import math

import pygame

BACKGROUND_COLOR=(36, 3, 70)
class PygameService:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((
            round(width),
            round(height)
        ))
        pygame.display.set_caption("Nathan's Food Chain")

    @staticmethod
    def check_user_quit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def clear_screen(self):
        self.surface.fill(BACKGROUND_COLOR)

    def _translate_xy(self, x, y):
        return (x, (self.height) - y)

    def draw_plant(self, plant):
        for p in plant:
            pygame.draw.circle(
                self.surface,
                p.color,
                (self._translate_xy(p.x, p.y)),
                p.get_radius()
            )

    def draw_cells(self, cells):
        for c in cells:
            self._draw_cell(c)

    def _draw_cell(self, cell):
        # Draw body
        pygame.draw.circle(
            self.surface,
            cell.color,
            (self._translate_xy(cell.x, cell.y)),
            cell.get_radius(),
            0 if not cell.eats_animals else round(.1 * cell.get_radius())
        )
        # Draw eyes
        eye_rad_offset = math.pi / 8
        offset_x_left = math.cos(cell.direction + eye_rad_offset) * cell.get_radius() * .8
        offset_y_left = math.sin(cell.direction + eye_rad_offset) * cell.get_radius() * .8
        offset_x_right = math.cos(cell.direction - eye_rad_offset) * cell.get_radius() * .8
        offset_y_right = math.sin(cell.direction - eye_rad_offset) * cell.get_radius() * .8
        pygame.draw.circle(
            self.surface,
            (255, 255, 255),
            (self._translate_xy(cell.x + offset_x_left, cell.y + offset_y_left)),
            .2 * cell.get_radius()
        )
        pygame.draw.circle(
            self.surface,
            (0, 0, 0),
            (self._translate_xy(cell.x + offset_x_left / .8 * .9, cell.y + offset_y_left / .8 * .9)),
            .08 * cell.get_radius()
        )
        pygame.draw.circle(
            self.surface,
            (255, 255, 255),
            (self._translate_xy(cell.x + offset_x_right, cell.y + offset_y_right)),
            .2 * cell.get_radius()
        )
        pygame.draw.circle(
            self.surface,
            (0, 0, 0),
            (self._translate_xy(cell.x + offset_x_right / .8 * .9, cell.y + offset_y_right / .8 * .9)),
            .08 * cell.get_radius()
        )

