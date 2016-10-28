import pygame
from random import randint, choice
import math
import os


class Obstacle():
    def __init__(self):
        pygame.init()
        self.SQRT3 = math.sqrt(3)
        self.scale = int(math.floor(math.sqrt(6) * 5))
        self.pos = ()
        self.position = ()
        self.ob1 = pygame.image.load(os.path.join(os.path.dirname(__file__), "image/Obstacle/1.png"))
        self.ob1 = pygame.transform.scale(self.ob1, (self.scale, self.scale))
        self.ob2 = pygame.image.load(os.path.join(os.path.dirname(__file__), "image/Obstacle/2.png"))
        self.ob2 = pygame.transform.scale(self.ob2, (self.scale, self.scale))
        self.ob3 = pygame.image.load(os.path.join(os.path.dirname(__file__), "image/Obstacle/3.png"))
        self.ob3 = pygame.transform.scale(self.ob3, (self.scale, self.scale))
        self.ob = (self.ob1, self.ob2, self.ob3)

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

    def display(self, screen, a, pos):
        screen.blit(self.ob[a], self.ConvertPosition(pos))

