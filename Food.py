import pygame
from random import randint, choice
import math
import os


class Food():
    def __init__(self):
        pygame.init()
        # self.grid = grid()
        self.SQRT3 = math.sqrt(3)
        self.scale = int(math.floor(math.sqrt(6) * 5))
        self.pos = ()
        # self.foodImage = None
        self.position = ()
        self.foodImage = pygame.image.load(os.path.join(os.path.dirname(__file__), "image/food.png"))
        self.foodImage = pygame.transform.scale(self.foodImage, (self.scale, self.scale))
        # self.size = (840, 780)
        # self.foodSurface = pygame.Surface(self.size)

    def set_pos(self):
        x = randint(1, 40)
        if x % 2 == 0:
            y = choice(range(2, 80, 2))
        else:
            y = choice(range(1, 80, 2))
        self.pos = (x, y)
        print self.pos

    def ConvertPosition(self, pos):
        # if pos[1] % 2 == 1:
        self.position = (15 * pos[0] + 5, 5.0 * self.SQRT3 * pos[1] + 10)
        # elif pos[1] % 2 == 0:
        #     self.position = (15 * pos[0] + 10, 5.0 * self.SQRT3 * pos[1] + 15)
        return self.position

    def display(self, screen):
        screen.blit(self.foodImage, self.ConvertPosition(self.pos))

