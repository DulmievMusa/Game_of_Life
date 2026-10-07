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
    ("slower", pygame.Rect(190, height + 10, 50, 40)),
    ("faster", pygame.Rect(250, height + 10, 50, 40)),
    ("clear", pygame.Rect(730, height + 10, 50, 40)),
    ("torus", pygame.Rect(530, height + 10, 180, 40)),
]



def main():
    pygame.init()
    font = pygame.font.SysFont("Arial", 22)
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

    step_interval = iteration_time
    STEP_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(STEP_EVENT, step_interval)
    clock = pygame.time.Clock()
    paused = True
    toroidal = False
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
                            elif action == "clear":
                                paused = True
                                for row in matrix:
                                    for x in range(len(row)):
                                        row[x] = 0
                            elif action == "slower":
                                step_interval = min(5000, int(step_interval * 1.3))
                                pygame.time.set_timer(STEP_EVENT, step_interval)

                            elif action == "faster":
                                step_interval = max(10, int(step_interval / 1.3))
                                pygame.time.set_timer(STEP_EVENT, step_interval)
                            elif action == "torus":
                                toroidal = not toroidal
                            break

            elif event.type == STEP_EVENT:
                if not paused:
                    matrix = take_step(matrix, birth=birth, survival=survival, toroidal=toroidal)

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

            if action == "torus":
                label = "Тор: вкл" if toroidal else "Тор: выкл"
                text = font.render(label, True, (255, 255, 255))
                screen.blit(text, text.get_rect(center=rect.center))
        speed_percent = 10 / step_interval * 100

        speed_text = font.render(
            f"Скорость: {speed_percent:.1f}%",
            True,
            (255, 255, 255)
        )

        screen.blit(speed_text, (320, height + 20))
        pygame.display.flip()

        clock.tick(120)

    
    


if __name__ == '__main__':
    main()
