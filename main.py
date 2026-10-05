import pygame
from pygame.locals import *

width = 800
height = 700
size = 20


def draw_cellular_field(matrix, background, size):
    for y in range(int(height / size)):
        for x in range(int(width / size)):
            if matrix[y][x] == 1:
                pygame.draw.rect(background, (250, 250, 250), (x * size, y * size, size, size), 0)
            else:
                pygame.draw.rect(background, (250, 250, 250), (x * size, y * size, size, size), 1)
    return background

    

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

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        background = draw_cellular_field(matrix, background, size)
        pygame.display.flip()

    
    


if __name__ == '__main__':
    main()