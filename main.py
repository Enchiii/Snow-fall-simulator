import pygame
import random

pygame.init()

NUM_SNOW = 150
WIDTH = 800
HEIGHT = 600
speed = 2

screen = pygame.display.set_mode([WIDTH, HEIGHT])

snow_list = []

for i in range(NUM_SNOW):
    snow_list.append([random.randint(0, WIDTH), random.randint(
        0, HEIGHT), random.randint(1, 4)])


is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 0))

    for snow in snow_list:
        pygame.draw.circle(screen, (255, 255, 255),
                           (snow[0], snow[1]), snow[2])
        snow[1] += speed

    pygame.display.flip()

pygame.quit()
