import turtle
import pygame as pg
import time

pg.mixer.init()
pg.init()
pg.mixer.set_num_channels(500)

#Polyrhythm is the simplified ratio of the dimentions of the board 
dimxs = [60] #Widths of the board
dimys = [61] #Heigts of the board
speeds = [0] #Speeds to run the animation at (1-10)
Stupid = False
if Stupid == True:
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
else:
    colors = ["red", "blue"]

topRight = 45
topLeft = 135
bottomLeft = 225
bottomRight = 315

Top = pg.mixer.Sound("Audio files/Top.wav")
Side = pg.mixer.Sound("Audio files/Side.wav")
Corner = pg.mixer.Sound("Audio files/corner.wav")

for iter in range(len(dimxs)):
    dimx = dimxs[iter]
    dimy = dimys[iter]
    turtle.color("black")
    turtle.screensize(dimx,dimy)
    turtle.penup()
    turtle.goto(-dimx,-dimy)
    turtle.pendown()
    turtle.speed(0)
    turtle.goto(-dimx,-dimy)
    turtle.goto(-dimx, dimy)
    turtle.goto(dimx,dimy)
    turtle.goto(dimx, -dimy)
    turtle.goto(-dimx, -dimy)
    turtle.penup()
    turtle.goto(-dimx + 1, -dimy + 1)
    turtle.pendown()
    turtle.hideturtle()
    turtle.speed(speeds[iter])

    sideHits = 0
    topBottomHits = 0
    running = True
    direcc = 45
    colorn = 0

    def distanceToRWall():
        return turtle.distance(dimx, y)
    def distanceToLWall():
        return turtle.distance(-dimx, y)
    def distanceToTop():
        return turtle.distance(x, dimy)
    def distanceToBottom():
        return turtle.distance(x, -dimy)
    def closerToTop():
        if direcc == topLeft or direcc == bottomLeft:
            return distanceToLWall() > distanceToTop()
        else:
            return distanceToRWall() > distanceToTop()
    def closerToBottom():
        if direcc == topLeft or direcc == bottomLeft:
            return distanceToLWall() > distanceToBottom()
        else:
            return distanceToRWall() > distanceToBottom()

    time.sleep(3)

    while running == True:
        if colorn > len(colors) - 1:
            colorn = 0
        if direcc > 360:
            direcc -= 360
        if direcc < 0:
            direcc += 360
        posit = turtle.pos()
        x = round(int(posit[0]))
        y = round(int(posit[1]))
        turtle.color(colors[colorn])
        #debug stuffs
        #print(f'--------\ndirec is {direcc}')
        #print(f'direcc is {direcc}')
        #print(f'distance to bottom {distanceToBottom()}')
        #print(f'distance to top {distanceToTop()}')
        #print(f'distance to rwall {distanceToRWall()}')
        #print(f'distance to lwall {distanceToLWall()}')
        #print(f'position is {posit}')
        print(f'{sideHits}:{topBottomHits}')
        if direcc == bottomLeft:
            if closerToBottom():
                colorn += 1
                turtle.goto(x - distanceToBottom(), y - distanceToBottom())
                #print(f'moving to {x - distanceToBottom()}, {y - distanceToBottom()}')
                direcc -= 90
                topBottomHits += 1
                Top.play()
            else:
                colorn += 1
                turtle.goto(x - distanceToLWall(), y - distanceToLWall())
                #print(f'moving to {x - distanceToLWall()}, {y - distanceToLWall()}')
                direcc += 90
                sideHits += 1
                Side.play()
        elif direcc == topLeft:
            if closerToTop():
                colorn += 1
                turtle.goto(x - distanceToTop(), y + distanceToTop())
                #print(f'moving to {x - distanceToTop()}, {y + distanceToTop()}')
                direcc += 90
                topBottomHits += 1
                Top.play()
            else:
                colorn += 1
                turtle.goto(x - distanceToLWall(), y + distanceToLWall())
                #print(f'moving to {x - distanceToLWall()}, {y + distanceToLWall()}')
                direcc -= 90
                sideHits += 1
                Side.play()
        elif direcc == topRight:
            if closerToTop():
                colorn += 1
                turtle.goto(x + distanceToTop(), y + distanceToTop())
                #print(f'moving to {x} + {distanceToTop()}, {y} + {distanceToTop()}')
                direcc -= 90
                topBottomHits += 1
                Top.play()
            else:
                colorn += 1
                turtle.goto(x + distanceToRWall(), y + distanceToRWall())
                #print(f'moving to {x} + {distanceToRWall()}, {y} + {distanceToRWall()}')
                direcc += 90
                sideHits += 1
                Side.play()
        elif direcc == bottomRight:
            if closerToBottom():
                colorn += 1
                turtle.goto(x + distanceToBottom(), y - distanceToBottom())
                #print(f'moving to {x + distanceToBottom()}, {y - distanceToBottom()}')
                direcc += 90
                topBottomHits += 1
                Top.play()
            else:
                colorn += 1
                turtle.goto(x + distanceToRWall(), y - distanceToRWall())
                #print(f'moving to {x + distanceToRWall()}, {y - distanceToRWall()}')
                direcc -= 90
                sideHits += 1
                Side.play()
        if x == dimx and y == -dimy:
            Corner.play()
            running = False
        if x == dimx and y == dimy:
            Corner.play()
            running = False
        if x == -dimx and y == -dimy:
            Corner.play()
            running = False
        if x == -dimx and y == dimy:
            Corner.play()
            running = False
    print(str(topBottomHits) + ":" + str(sideHits))
    time.sleep(5)
    turtle.clear()


