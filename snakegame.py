import pygame as pg
import time
import random

pg.init()

white = (255,255,255)
black = (0,0,0)
blue = (55,150,215)
green = (124,252,0)

dis_w = 800
dis_h = 600

dis = pg.display.set_mode((dis_w, dis_h))

clock = pg.time.Clock()

snake_block = 20
snake_speed = 15
score = 0

font_style = pg.font.SysFont("arial",20)
score_font = pg.font.SysFont("arial",20)

def snake(snake_block, snake_list): 
    """snake test"""
    for x in snake_list: 
        pg.draw.rect(dis,white,[x[0],x[1], snake_block, snake_block])

# def stats(score):
#     self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
#     pg.display.update()

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_w / 2
    y1 = dis_h / 2

    x1_change = 0
    y1_change = 0

    snakeList = []
    snakeLength = 1

    bitx = round(random.randrange(0,dis_w - snake_block)/snake_block)*snake_block
    bity = round(random.randrange(0,dis_h - snake_block)/snake_block)*snake_block

    while not game_over:
        dis.fill(black)
        snake(snake_block,snakeList) #calling function that draws snakeList for every x - coordinate 
        pg.draw.rect(dis,green,[bitx,bity,snake_block,snake_block])

        for event in pg.event.get():
            if event.type == pg.quit:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pg.K_UP:
                    x1_change = 0
                    y1_change = snake_block
                if event.key == pg.K_DOWN:
                    x1_change = 0
                    y1_change = -snake_block

        x1 += x1_change
        y1 -= y1_change

        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        if x1 == bitx and y1 == bity: 
            """if snake head coordinates == bit coordinates""" 
            bitx = round(random.randrange(0,dis_w - snake_block)/snake_block)*snake_block
            bity = round(random.randrange(0,dis_h - snake_block)/snake_block)*snake_block
            snakeLength += 1

        for x in snakeList[:-1]: #from this to the (:) end of the list (-1)
            if x == snakeHead:
                game_over = True

        if x1 >= dis_w or x1 < 0 or y1 >= dis_h or y1 < 0: #borders
            game_over = True

        pg.display.update()
        clock.tick(snake_speed)

gameLoop()


