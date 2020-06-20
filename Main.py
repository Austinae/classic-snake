import pygame
import random

# Initiate pyGame library system
pygame.init()

gameTitle = "Slither"

# Sets windows title and the icon as a second argument
pygame.display.set_caption(gameTitle)

imgSnakeHead = pygame.image.load("snakeHead.png")
imgSnakeBody = pygame.image.load("snakeBody.png")
imgSnakeTail = pygame.image.load("snakeTail.png")

canvasWidth = 800
canvasHeight = 600
fps = 13

direction = "right"

# This creates the window for the game according to a specified width and height in pixels
canvas = pygame.display.set_mode((canvasWidth, canvasHeight))

colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)
colorRed = (255, 0, 0)
colorGreen = (0, 255, 0)
colorBlue = (0, 0, 255)

backgroundColour = colorWhite

font = pygame.font.SysFont(None, 25)

""" Update entire canvas with pygame.display.flip(). However, if you want to update only specific areas that you mention
(better performance) then use pygame.display.update(). When you add no parameters to update then it acts like flip, 
that's why flip is so rarely used"""

# This is where you take care of events and where you put all your code

blockSize = 10


def message_to_screen(message, colour):
    text = font.render(message, True, colour)
    canvas.blit(text, [canvasWidth/2, canvasHeight/2])


def snake(blockSize, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(imgSnakeHead, 270)
        tail = pygame.transform.rotate(imgSnakeTail, 270)
    if direction == "left":
        head = pygame.transform.rotate(imgSnakeHead, 90)
        tail = pygame.transform.rotate(imgSnakeTail, 90)
    if direction == "up":
        head = imgSnakeHead
        tail = imgSnakeTail
    if direction == "down":
        head = pygame.transform.rotate(imgSnakeHead, 180)
        tail = pygame.transform.rotate(imgSnakeTail, 180)
    canvas.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for snake in snakeList[1:-1]:
        canvas.blit(imgSnakeBody, (snake[0], snake[1]))
    if len(snakeList)>1:
        canvas.blit(tail, (snakeList[0][0], snakeList[0][1]))



def gameLoop():

    global direction

    snakeList = []
    snakeLength = 1

    gameRunning = True
    playing = True

    x = 300
    y = 300

    p = 10
    pp = 0

    appleX = random.randrange(0, canvasWidth - blockSize, blockSize)
    appleY = random.randrange(0, canvasHeight - blockSize, blockSize)

    while gameRunning:
        while not playing:
            canvas.fill(colorWhite)
            message_to_screen("Game over, press C to play again or A to quit", colorRed)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameRunning = False
                        playing = True
                    if event.key == pygame.K_c:
                        gameLoop()

        # This is why pyGame is awesome. It takes care of all the events handling on it's own through pygame.event.get()
        # This returns a tuple with a bunch of data like button pressed or many other things, check documentation
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameRunning = False
                elif event.key == pygame.K_LEFT:
                    direction = "left"
                    pp = 0
                    p = -blockSize
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    pp = 0
                    p = blockSize
                elif event.key == pygame.K_UP:
                    direction = "up"
                    p = 0
                    pp = -blockSize
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    p = 0
                    pp = blockSize
            elif event.type == pygame.QUIT:
                gameRunning = False

        if x >= canvasWidth or x < 0 or y >= canvasHeight or y < 0:
            playing = False

        x += p
        y += pp
        # Changes canvas background
        canvas.fill(backgroundColour)
        pygame.draw.rect(canvas, colorRed, [appleX, appleY, blockSize, blockSize])

        snakeHead = [x, y]
        snakeList.append(snakeHead)

        if len(snakeList)>snakeLength:
            del snakeList[0]

        for segment in snakeList[:-1]:
            if segment == snakeHead:
                playing = False

        snake(blockSize, snakeList)

        pygame.display.update()

        if x == appleX and y == appleY:
            snakeLength += 1
            appleX = random.randrange(0, canvasWidth - blockSize, blockSize)
            appleY = random.randrange(0, canvasHeight - blockSize, blockSize)


        # Frames per second
        pygame.time.Clock().tick(fps)

    # Use pygame.quit() to delete all initialized variables and then quit() to stop main pyGame loop
    pygame.quit()

    quit()

gameLoop()