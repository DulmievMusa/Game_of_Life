from funcs import *
import pygame
from pygame.locals import *

width = 800
height = 700
size = 10
iteration_time = 100

# RULES
birth = [3]
survival = [2, 3]




def main():

    pygame.init()
    matrix = [[0 for i in range(int(width / size))] for j in range(int(height / size))]
    # matrix = fill_random(matrix)
    # fill_random(matrix)
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
    paused = True
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

        if paused:
            left, _, right = pygame.mouse.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()

            x = mouse_x // size
            y = mouse_y // size

            if 0 <= y < len(matrix) and 0 <= x < len(matrix[y]):
                if left:
                    matrix[y][x] = 1
                elif right:
                    matrix[y][x] = 0

        background.fill((0, 0, 0))
        draw_cellular_field(matrix, background, size)
        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock.tick(120)

    
    


if __name__ == '__main__':
    main()
