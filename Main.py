import HighScore
from Grid import grid
from Snake import Snake
from Food import Food
from Obstacles import Obstacle
from random import randint
import pygame
from pygame.locals import *
import sys
import math

pygame.init()

size = (840, 730)
body = [(1, 5), (1, 3), (1, 1)]
fieldScreen = pygame.display.set_mode(size)

grid = grid()
snake = Snake(body)
food = Food()
obstacle = Obstacle()
white = (255, 255, 255)
black = (0, 0, 0)


key_dict = {pygame.K_o: (0, 2), pygame.K_i: (-1, 1), pygame.K_q: (-1, -1), pygame.K_w: (0, -2),
            pygame.K_e: (1, -1), pygame.K_p: (1, 1)}
rdict = {(0, 2): pygame.K_o, (-1, 1): pygame.K_i, (-1, -1): pygame.K_q, (0, -2): pygame.K_w,
         (1, -1): pygame.K_e, (1, 1): pygame.K_p}
oppositedict = {(0, 2): (0, -2), (-1, 1): (1, -1), (-1, -1): (1, 1), (0, -2): (0, 2),
         (1, 1): (-1, -1), (1, -1): (-1, 1)}

score = 0

food.set_pos()
obstacle.set_pos()
a = randint(0, 2)
ranImage = [a]
ran = [obstacle.pos]

grid.draw_grid(fieldScreen)
snake.draw_score(fieldScreen, score)
# pygame.display.flip()

Difficulty = 0

while True:
    # food.display(fieldScreen)
    # obstacle.display(fieldScreen)
    # pygame.display.update()
    grid.draw_grid(fieldScreen)
    food.display(fieldScreen)
    for i in range(0, len(ran)):
        obstacle.display(fieldScreen, ranImage[i], ran[i])
    snake.draw_score(fieldScreen, score)
    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == KEYDOWN:
            pressed_key = event.key
            # print pressed_key
            if key_dict.has_key(pressed_key) and not pressed_key == rdict[snake.dir]:
                if not key_dict[pressed_key] == oppositedict[snake.dir]:
                    snake.change_direction(key_dict[pressed_key])

        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            xPos = pos[0]
            yPos = pos[1]
            if (680 <= xPos <= 810 and 300 <= yPos <= 350):
                snake.status.reverse()

    snake.move()
    new = snake.new

    if not snake.status[0] == 'stop':
        if not food.pos == snake.head:
            body.pop()
        else:
            food.set_pos()
            while food.pos in body:
                food.set_pos()
            # food.display(fieldScreen)

            score += 1
            # snake.draw_score(fieldScreen, score)

            if Difficulty < 25:
                Difficulty += 1

            for i in range(0, 2):
                a = randint(0, 2)
                obstacle.set_pos()
                while obstacle.pos in (body or ran):
                    obstacle.set_pos()
                ran.append(obstacle.pos)
                ranImage.append(a)
            # for i in range(0, len(ran)):
            #     obstacle.display(fieldScreen, ranImage[i], ran[i])
            #     pygame.display.update()



        if new[0] <= 0 or new[1] <= 0 or new[0] >= 41 or new[1] >= 81:
            snake.gameOver = True
        elif new in body:
            snake.gameOver = True
        elif new in ran:
            snake.gameOver = True
        else:
            body.insert(0, new)

            snake = Snake(body)
            snake.display(fieldScreen)
            pygame.display.update()

        speed = 100 - int((math.floor(Difficulty / 5.0) - 1) * 5)
        pygame.time.wait(speed)

    if snake.gameOver:

        HighScore.add(score)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        HighScore.ScoreScreen()

            fieldScreen = pygame.display.set_mode((240, 420))
            fieldSurface = pygame.Surface((240, 420))
            fieldSurface.fill(black)
            scoreFont = pygame.font.SysFont("Arial", 30)
            text1 = "Game Over!"
            text2 = "Your score: %d" % score
            text3 = "Click Space"
            text4 = "for High Scores"

            scoreText1 = scoreFont.render(text1, True, white)
            width1 = scoreText1.get_rect().width
            height1 = scoreText1.get_rect().height

            scoreText2 = scoreFont.render(text2, True, white)
            width2 = scoreText2.get_rect().width
            height2 = scoreText2.get_rect().height

            scoreText3 = scoreFont.render(text3, True, white)
            width3 = scoreText3.get_rect().width
            height3 = scoreText3.get_rect().height

            scoreText4 = scoreFont.render(text4, True, white)
            width4 = scoreText4.get_rect().width
            height4 = scoreText4.get_rect().height

            fieldSurface.blit(scoreText1, (120 - width1 / 2, 100 - height1 / 2))
            fieldSurface.blit(scoreText2, (120 - width2 / 2, 200 - height2 / 2))
            fieldSurface.blit(scoreText3, (120 - width3 / 2, 300 - height3 / 2))
            fieldSurface.blit(scoreText4, (120 - width4 / 2, 320 - height4 / 2))

            fieldScreen.blit(fieldSurface, (0, 0))
            pygame.display.flip()



