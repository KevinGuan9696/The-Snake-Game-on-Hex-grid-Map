# from Grid import *
# from Food import Food
import math
import pygame
import os


class Snake():

    def __init__(self, body):
        pygame.init()
        # self.grid = grid()
        # self.body = [(1, 5), (1, 3), (1, 1)]
        self.direction = ((0, 2), (-1, 1), (-1, -1), (0, -2), (1, 1), (1, -1))
        self.status = ['run', 'stop']
        # self.speed = 300
        # self.food = Food()
        self.gameOver = False

        self.body = body
        self.head = self.body[0]
        self.headnext = self.body[1]
        self.dir = (self.head[0] - self.headnext[0], self.head[1] - self.headnext[1])
        # self.score = 0
        self.SQRT3 = math.sqrt(3)
        self.scale = int(math.floor(math.sqrt(6) * 5))
        self.position = ()
        self.snakeImage = pygame.image.load(os.path.join(os.path.dirname(__file__), 'image/snakebase.png'))
        self.snakeImage = pygame.transform.scale(self.snakeImage, (self.scale, self.scale))
        self.snakeHeadImage = pygame.image.load(os.path.join(os.path.dirname(__file__), 'image/snakehead.png'))
        self.snakeHeadImage = pygame.transform.scale(self.snakeHeadImage, (self.scale, self.scale))
        self.new = ()
        self.size = (840, 780)
        self.snakeSurface = pygame.Surface(self.size)
        self.scoreSurface = pygame.Surface(self.size)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    def change_direction(self, direction):
        self.dir = direction

    def ConvertPosition(self, pos):
        # if pos[1] % 2 == 1:
        self.position = (15 * pos[0] + 5, 5.0 * self.SQRT3 * pos[1] + 10)
        # elif pos[1] % 2 == 0:
        #     self.position = (15 * pos[0] + 10, 5.0 * self.SQRT3 * pos[1] + 15)
        return self.position

    def display(self, screen):
        # self.grid.draw_grid()
        # self.grid.fieldSurface.blit(self.snakeHeadImage, self.ConvertPosition(self.body[0]))
        # for i in range(1, len(self.body)):
        #     position = self.ConvertPosition(self.body[i])
        #     self.grid.fieldSurface.blit(self.snakeImage, position)
        # self.grid.fieldScreen.blit(self.grid.fieldSurface, (0, 0))
        # pygame.display.update()
        screen.blit(self.snakeHeadImage, self.ConvertPosition(self.body[0]))
        for i in range(1, len(self.body)):
            position = self.ConvertPosition(self.body[i])
            screen.blit(self.snakeImage, position)

    def move(self):
        #((0, 2), (-1, 1), (-1, -1), (0, -2), (1, 1), (1, -1))
        #Down
        if self.dir == self.direction[0]:
            self.new = (self.head[0], self.head[1] + 2)
        # LeftUp
        elif self.dir == self.direction[1]:
            self.new = (self.head[0] - 1, self.head[1] + 1)
        # LeftDown
        elif self.dir == self.direction[2]:
            self.new = (self.head[0] - 1, self.head[1] - 1)
        #Up
        elif self.dir == self.direction[3]:
            self.new = (self.head[0], self.head[1] - 2)
        #RightUp
        elif self.dir == self.direction[4]:
            self.new = (self.head[0] + 1, self.head[1] + 1)
        #RIghtDown
        else:
            self.new = (self.head[0] + 1, self.head[1] - 1)

    def draw_score(self, screen, score):
        scoreNumFont = pygame.font.SysFont("Arial", 30)
        scoreNumText = scoreNumFont.render("%d" % score, True, self.white)
        screen.blit(scoreNumText, (680, 630))
