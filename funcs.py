import random
import pygame
from pygame.locals import *

def fill_random(matrix):
    for row in matrix:
        for x in range(len(row)):
            row[x] = random.randint(0, 1)
    return matrix


def draw_cellular_field(matrix, background, size):
    rows = len(matrix)
    columns = len(matrix[0])
    for y in range(rows):
        for x in range(columns):
            if matrix[y][x] == 1:
                pygame.draw.rect(background, (250, 250, 250), (x * size, y * size, size, size), 0)
            else:
                pygame.draw.rect(background, (250, 250, 250), (x * size, y * size, size, size), 1)
    return background

def take_step(matrix):
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

            if neighbors == 3 or (matrix[y][x] == 1 and neighbors == 2):
                next_matrix[y][x] = 1

    return next_matrix  

def fill_random(matrix):
    for row in matrix:
        for x in range(len(row)):
            row[x] = random.randint(0, 1)
    return matrix