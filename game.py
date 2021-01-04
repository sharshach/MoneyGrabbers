import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000,650))
pygame.display.set_caption("Money Grabber")
icon = pygame.image.load('dollar.png')
pygame.display.set_icon(icon)
# scoring
score=0
lives=5
font = pygame.font.Font('freesansbold.ttf', 32)
def show_score(x, y):
    scoreRender = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(scoreRender, (x, y))
def show_lives(x,y):
    livesRender = font.render("lives : " + str(lives), True, (255, 255, 255))
    screen.blit(livesRender, (x, y))
def gameOver(x,y):
    screen.fill((0,0, 0))
    gameOverRender = font.render("Game Over  ", True, (255, 255, 255))
    screen.blit(gameOverRender, (x, y))
    scoreRender = font.render("press the cross symbol to close game" , True, (255, 255, 255))
    screen.blit(scoreRender, (x, y+50))
    hintRender = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(hintRender, (x, y+100))
    

# bucket
bucketImg = pygame.image.load('bucket.png')
bucketImg = pygame.transform.scale(bucketImg,(64,64))
bucketX=470
bucketY=550
bucketXchange=0.5
bucketCurrentChange=0
def bucket(x, y):
    screen.blit(bucketImg, (x, y))
def bucketPositionUpdate(bucketCurrentChange):
    global bucketX
    bucketX+=bucketCurrentChange
    if bucketX<0:
        bucketX=0
    if bucketX>1000-64:
        bucketX=1000-64

#coin
coinImg = pygame.image.load('dollar.png')
coinImg = pygame.transform.scale(coinImg,(32,32))
coinX=random.randint(0,1000-64)
coinY=0
coinYchange=0.2
coinSpeedIncrement=0.05
def coin(x, y):
    screen.blit(coinImg, (x, y))
def coinPositionUpdate():
    global coinY,coinX,lives,score,coinYchange
    coinY+=coinYchange
    if(coinY>=550-32):
        if(coinX>=bucketX-10 and coinX+32<=bucketX+72):
            score+=1
            if(score%5==0):
                coinYchange+=coinSpeedIncrement
        else:
            lives-=1
        coinX=random.randint(0,1000-64)
        coinY=0


isRunning=True
while isRunning:
    screen.fill((0,0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bucketCurrentChange = -bucketXchange
            if event.key == pygame.K_RIGHT:
                bucketCurrentChange = +bucketXchange

        if event.type == pygame.KEYUP:
            bucketCurrentChange=0

    bucketPositionUpdate(bucketCurrentChange) 
    coinPositionUpdate()
    coin(coinX,coinY)
    bucket(bucketX,bucketY)
    show_score(800,0)
    show_lives(600,0)
    if(lives<0):
        gameOver(200,200)
    pygame.display.update()

pygame.quit()