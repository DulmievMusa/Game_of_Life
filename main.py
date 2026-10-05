import random
from funcs import *
import pygame
from pygame.locals import *

width = 800
height = 700
size = 20
iteration_time = 100






def main():
    # Initialise screen
    pygame.init()
    matrix = [[0 for i in range(int(width / size))] for j in range(int(height / size))]
    matrix = fill_random(matrix)
    fill_random(matrix)
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
