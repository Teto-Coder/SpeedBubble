import sys
import pygame
import time
import random
from pygame.locals import QUIT
from Object import *


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (0,0,0)
clock = pygame.time.Clock()
bubble_radius = 30
HIGH_SCORE_FILE = open('highscore.txt','r')
highscore = HIGH_SCORE_FILE.read()

window_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
window_surface.fill(BACKGROUND_COLOR)


def resetGame():
    global game_mode , bubbleGroup , curClick , bubbleNumber , startButton
    game_mode = 0
    curClick = bubbleNumber = 50
    bubbleGroup = pygame.sprite.Group()
    btnSizeX = 200
    btnSizeY = 48
    startButton = Button(window_surface,[SCREEN_WIDTH/2-btnSizeX/2,SCREEN_HEIGHT/2,btnSizeX,btnSizeY],'RESTART')
    for i in range(0,8):
        bubbleGroup.add(Bubble(window_surface , [random.randint(bubble_radius,SCREEN_WIDTH - bubble_radius-10)+10,random.randint(bubble_radius,SCREEN_HEIGHT - bubble_radius-10)+10] , bubble_radius , bubbleNumber))
        bubbleNumber -= 1

resetGame()

#bubble = Bubble(window_surface , [random.randint(bubble_radius,SCREEN_WIDTH - bubble_radius),random.randint(bubble_radius,SCREEN_HEIGHT - bubble_radius)] , bubble_radius , curClick)




highScoreText = pygame.font.SysFont("None", 40)
scoreText = pygame.font.SysFont("None", 40)
timerText = pygame.font.SysFont("None", 25)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(game_mode == 2 and startButton.getRect()[0] < pygame.mouse.get_pos()[0] < startButton.getRect()[0] + startButton.getRect()[2] and startButton.getRect()[1] < pygame.mouse.get_pos()[1] < startButton.getRect()[1] + startButton.getRect()[3]):
                resetGame()
            for ele in bubbleGroup:
                if ele.getPos()[0] - bubble_radius < pygame.mouse.get_pos()[0] < ele.getPos()[0] + bubble_radius and ele.getPos()[1] - bubble_radius < pygame.mouse.get_pos()[1] < ele.getPos()[1] + bubble_radius and ele.number == curClick:
                    if(game_mode == 0):
                        game_mode = 1
                        start = time.time()
                    bubbleGroup.remove(ele)
                    curClick -= 1
                    if(bubbleNumber>0):
                        bubbleGroup.add(Bubble(window_surface , [random.randint(bubble_radius,SCREEN_WIDTH - bubble_radius),random.randint(bubble_radius,SCREEN_HEIGHT - bubble_radius)] , bubble_radius , bubbleNumber))
                        bubbleNumber -= 1
                    break
                #bubble.kill()
                # bubble.setX(random.randint(bubble_radius,SCREEN_WIDTH - bubble_radius))
                # bubble.setY(random.randint(bubble_radius,SCREEN_HEIGHT - bubble_radius))
            if(curClick == 0):
                end = time.time()
                game_mode = 2
                startButton.setVisible(True)
    window_surface.fill(BACKGROUND_COLOR)
    if(game_mode == 0):
        timerBoard = timerText.render("00:00.00",True, (255,255,255))
    else:
        nowTime = time.time()
        timerBoard = timerText.render(str(format(int((nowTime-start)/60),'02d'))+':'+format((nowTime-start)%60,'05.2f'),True, (255,255,255))
    if(game_mode == 2):
        curScore = str(format(int((end-start)/60),'02d'))+':'+format((end-start)%60,'05.2f')
        scoreboard = scoreText.render('Spend Time: '+curScore, True,(255,255,255))
        highscoreboard = highScoreText.render('Highest Score: '+ min(curScore,highscore) , True,(255,255,255))
        HIGH_SCORE_FILE = open('highscore.txt','w')
        HIGH_SCORE_FILE.write(min(curScore,highscore))
        HIGH_SCORE_FILE.close()
        window_surface.blit(scoreboard,(SCREEN_WIDTH/2-scoreboard.get_width()/2,SCREEN_HEIGHT/2-scoreboard.get_height()*1.5))
        window_surface.blit(highscoreboard,(SCREEN_WIDTH/2-highscoreboard.get_width()/2,SCREEN_HEIGHT/2-highscoreboard.get_height()*3))
        startButton.update()
    else:
        window_surface.blit(timerBoard,(10,10))
        bubbleGroup.update()
    pygame.display.update()
    #pygame.time.delay(1000) 
    clock.tick(60)