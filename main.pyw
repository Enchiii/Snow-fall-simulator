import copy
import pygame
import random

random.seed(12)

pygame.init()

NUM_SNOW = 300
W_WIDTH, W_HEIGHT = 800, 600

window = pygame.display.set_mode([W_WIDTH, W_HEIGHT])
clock = pygame.time.Clock()

class SNOW:
    X_SPEED, Y_SPEED = 1, 2
    floor = [[] for _ in range(W_WIDTH)]

    def __init__(self):
        self.pos_x = random.randint(0, W_WIDTH)
        self.pos_y = random.randint(0, W_HEIGHT)
        self.size = random.randint(1, 3)
        self.anim_state = 0
        self.anim_duration = random.randint(100, 200)
        self.anim_direction = random.getrandbits(1)
        self.falling = True

    def reset(self):
        self.pos_x = random.randint(0, W_WIDTH)
        self.pos_y = 0
        self.size = random.randint(1, 3)
        self.anim_state = 0
        self.anim_duration = random.randint(100, 200)
        self.anim_direction = random.getrandbits(1)
        self.falling = True

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.pos_x, self.pos_y), self.size)

    def update(self):
        if not self.falling:
            return

        self.anim_state += 1

        if self.anim_state == self.anim_duration:
            self.anim_state = 0
            self.anim_direction = not self.anim_direction

        new_pos_x = self.pos_x + self.X_SPEED * (1 if self.anim_direction else -1)
        if new_pos_x > W_WIDTH - 1:
           new_pos_x = 0
        if new_pos_x < 0:
            new_pos_x = W_WIDTH - 1

        self.pos_x = new_pos_x
        self.pos_y += self.Y_SPEED

        if self.pos_y >= W_HEIGHT - len(self.floor[self.pos_x]):
            self.falling = False
            new_snow = copy.deepcopy(self)
            new_snow.pos_y = W_HEIGHT - len(self.floor[self.pos_x])
            heights = [len(x) for x in self.floor]
            average_height = sum(heights) / len(heights)
            if len(self.floor[self.pos_x]) <= average_height:
                self.floor[self.pos_x].append(new_snow)
            self.reset()

    def draw_floor(self, window):
        for x in self.floor:
            for snow in x:
                pygame.draw.circle(window, (255, 255, 255), (snow.pos_x, snow.pos_y), snow.size)

snow_list = [SNOW() for _ in range(NUM_SNOW)]

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window.fill((0, 0, 0))

    for snow in snow_list:
        snow.draw(window)
        snow.update()
    SNOW.draw_floor(SNOW, window)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
