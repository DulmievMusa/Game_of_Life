import pygame
from pygame.locals import *

width = 800
height = 700
size = 20
iteration_time = 100

def draw_cellular_field(matrix, background, size):
    for y in range(int(height / size)):
        for x in range(int(width / size)):
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




def main():
    # Initialise screen
    pygame.init()
    matrix = [[0 for i in range(int(width / size))] for j in range(int(height / size))]
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Basic Pygame program')
    

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Display some text
    # font = pygame.font.Font(None, 36)
    # text = font.render("Hello There", 1, (10, 10, 10))
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    matrix[3][5] = 1
    matrix[3][4] = 1
    matrix[3][6] = 1

    # Event loop
    STEP_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(STEP_EVENT, iteration_time)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == STEP_EVENT:
                matrix = take_step(matrix)


        background.fill((0, 0, 0))
        draw_cellular_field(matrix, background, size)
        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock.tick(120)

        pygame.display.flip()

    
    


if __name__ == '__main__':
    main()
