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

panel_height = 60


buttons = [
    ("start", pygame.Rect(10, height + 10, 50, 40)),
    ("pause", pygame.Rect(70, height + 10, 50, 40)),
    ("random", pygame.Rect(130, height + 10, 50, 40)),
]



def main():
    pygame.init()
    matrix = [[0 for i in range(int(width / size))] for j in range(int(height / size))]
    # matrix = fill_random(matrix)
    # fill_random(matrix)
    screen = pygame.display.set_mode((width, height + panel_height))
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for action, rect in buttons:
                        if rect.collidepoint(event.pos):
                            if action == "start":
                                paused = False
                            elif action == "pause":
                                paused = True
                            elif action == "random":
                                fill_random(matrix)
                                paused = True
                            break

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
        pygame.draw.rect(
        screen, (35, 35, 35),
        (0, height, width, panel_height)
        )

        mouse_pos = pygame.mouse.get_pos()

        for action, rect in buttons:
            color = (90, 90, 90) if rect.collidepoint(mouse_pos) else (60, 60, 60)
            pygame.draw.rect(screen, color, rect, border_radius=6)
            draw_button_icon(screen, action, rect)
        pygame.display.flip()

        clock.tick(120)

    
    


if __name__ == '__main__':
    main()
