import random
from funcs import *
import pygame
from pygame.locals import *

width = 800
height = 700
size = 20
iteration_time = 100

# RULES
birth = [3]
survival = [2, 3]




def main():

    pygame.init()
    matrix = [[0 for i in range(int(width / size))] for j in range(int(height / size))]
    matrix = fill_random(matrix)
    fill_random(matrix)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Basic Pygame program')
    

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    pygame.display.flip()


    STEP_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(STEP_EVENT, iteration_time)
    clock = pygame.time.Clock()
    paused = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

            elif event.type == STEP_EVENT:
                if not paused:
                    matrix = take_step(matrix, birth=birth, survival=survival)

        background.fill((0, 0, 0))
        draw_cellular_field(matrix, background, size)
        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock.tick(120)

    
    


if __name__ == '__main__':
    main()
