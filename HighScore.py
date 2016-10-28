import pygame
from pygame.locals import *
import os

white = (255, 255, 255)
black = (0, 0, 0)


HS = "Highscore.txt"


def ScoreScreen():
    ScoreScreen = pygame.display.set_mode((240, 420))
    ScoreSurface = pygame.Surface((240, 420))
    ScoreSurface.fill(black)
    ExitImage = pygame.image.load(os.path.join(os.path.dirname(__file__), 'image/Exit.png'))
    ScoreSurface.blit(ExitImage, (50, 355))
    ScoreScreen.blit(ScoreSurface, (0, 0))

    scoreFont = pygame.font.SysFont("Arial", 30)
    scoreText = scoreFont.render('Highscores', True, white)
    ScoreSurface.blit(scoreText, (15, 15))
    ScoreScreen.blit(ScoreSurface, (0, 0))

    scores = get()
    print scores
    for i in range(0, len(scores)):
        scoreFont = pygame.font.SysFont("Arial", 30)
        scoreText = scoreFont.render("No." + str(i + 1) + "                  " + str(scores[i].strip('\n')), True,
                                     white)
        ScoreSurface.blit(scoreText, (15, 15 + (int(i) + 1) * 30))
    ScoreScreen.blit(ScoreSurface, (0, 0))
    pygame.display.flip()

    notClicked = True
    while notClicked:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                xPos = pos[0]
                yPos = pos[1]
                if (50 <= xPos <= 150 and 370 <= yPos <= 420):
                    notClicked = not notClicked


def get():
    f = open(HS, "r")
    scores = []
    for line in f:
        scores.append(line)
    f.close()
    return scores


def add(s):
    f = open(HS, "r+")
    scores = get()
    scores.append(str(s) + "\n")
    scores.sort(reverse=True, key=int)
    f.truncate()
    for i in range(9):
        if i < len(scores):
            a = str(scores[i])
            f.write(a)
    f.close()
