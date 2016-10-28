import math
import pygame
import os

class grid():
    def __init__(self):
        pygame.init()
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.size = (840, 730)
        # self.fieldScreen = pygame.display.set_mode(self.size)
        self.fieldSurface = pygame.Surface(self.size)
        self.fieldSurface.fill(self.black)

        self.gridPoint = []
        self.SQRT3 = math.sqrt(3)

    def grid_point(self, m, n):
        if n % 2 == 1:
            self.gridPoint = [(5 * (2.0 * m + 2 * math.ceil(m / 2.0) - 3) + 15), (5 * (n - 1) * self.SQRT3 + 15)]
        elif n % 2 == 0:
            self.gridPoint = [(5 * (2.0 * m + 2 * math.ceil((m - 1) / 2.0) - 2) + 15), (5 * (n - 1) * self.SQRT3 + 15)]
        return self.gridPoint

    def draw_grid(self, screen):

        grey = (96, 96, 96)

        for m in range(1, 42):
            for n in range(1, 82):
                pygame.draw.line(self.fieldSurface, grey, self.grid_point(m, n), self.grid_point(m, n + 1))

        for n in range(1, 83):
            for m in range(1, 41, 2):
                pygame.draw.line(self.fieldSurface, grey, self.grid_point(m - (n % 2) + 1, n),
                                 self.grid_point(m - (n % 2) + 2, n))

        # self.fieldScreen.blit(self.fieldSurface, (0, 0))
        scoreFont = pygame.font.SysFont("Arial", 30)
        scoreText = scoreFont.render("Score: ", True, self.white)
        self.fieldSurface.blit(scoreText, (680, 600))
        screen.blit(self.fieldSurface, (0, 0))
        # self.fieldScreen.blit(self.fieldSurface, (0, 0))

        # pygame.display.flip()

        pauseImage = pygame.image.load(os.path.join(os.path.dirname(__file__), "image/Pause.png"))
        self.fieldSurface.blit(pauseImage, (680, 300))
