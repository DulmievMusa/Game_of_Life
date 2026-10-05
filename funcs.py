import random
import pygame
from pygame.locals import *


def draw_button_icon(surface, action, rect):
    color = (255, 255, 255)
    cx, cy = rect.center

    if action == "start":
        pygame.draw.polygon(surface, color, [
            (cx - 7, cy - 11),
            (cx - 7, cy + 11),
            (cx + 11, cy),
        ])

    elif action == "pause":
        pygame.draw.rect(surface, color, (cx - 9, cy - 10, 6, 20))
        pygame.draw.rect(surface, color, (cx + 3, cy - 10, 6, 20))

    elif action == "random":
        pygame.draw.rect(
            surface, color,
            (cx - 12, cy - 12, 24, 24),
            width=2, border_radius=4
        )

        for dx, dy in [(-6, -6), (6, -6), (0, 0), (-6, 6), (6, 6)]:
            pygame.draw.circle(surface, color, (cx + dx, cy + dy), 2)
    elif action in ("slower", "faster"):
        # Горизонтальная черта для обоих значков.
        pygame.draw.line(
            surface, color,
            (cx - 10, cy), (cx + 10, cy), 3
        )

        # Вертикальная черта превращает минус в плюс.
        if action == "faster":
            pygame.draw.line(
                surface, color,
                (cx, cy - 10), (cx, cy + 10), 3
            )

def fill_random(matrix):
    for row in matrix:
        for x in range(len(row)):
            row[x] = random.randint(0, 1)
    return matrix

def draw_cell_border(surface, color, rect, width=1):
    x, y, w, h = rect

    pygame.draw.line(
        surface, color,
        (x, y), (x + w - 1, y), width
    )
    pygame.draw.line(
        surface, color,
        (x, y), (x, y + h - 1), width
    )


def draw_cellular_field(matrix, background, size):
    rows = len(matrix)
    columns = len(matrix[0])
    for y in range(rows):
        for x in range(columns):
            if matrix[y][x] == 1:
                pygame.draw.rect(background, (250, 250, 250), (x * size, y * size, size, size), 0)
                # pygame.draw.rect(background, (0, 0, 0), (x * size, y * size, size, size), 1)     
                draw_cell_border(background, (0, 0, 0), (x * size, y * size, size, size))
            else:
                # pygame.draw.rect(background, (250, 250, 250), (x * size, y * size, size, size), 1)
                draw_cell_border(background, (250, 250, 250), (x * size, y * size, size, size))
    return background

def take_step(matrix, birth=[3], survival=[2]):
    rows = len(matrix)
    columns = len(matrix[0])
    next_matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    for y in range(rows):
        for x in range(columns):
            neighbors = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue
                    check_y = y + dy
                    check_x = x + dx
                    if 0 <= check_y < rows and 0 <= check_x < columns:
                        neighbors += matrix[check_y][check_x]

            if neighbors in birth or (matrix[y][x] == 1 and neighbors in survival):
                next_matrix[y][x] = 1

    return next_matrix  

def fill_random(matrix):
    for row in matrix:
        for x in range(len(row)):
            row[x] = random.randint(0, 1)
    return matrix