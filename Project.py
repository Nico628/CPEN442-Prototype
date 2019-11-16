import sys
import pygame
import os
import time

screen = pygame.display.set_mode((0, 0))
pos = (0, 0)

# grabbing the image to return
def get_image(path):
        image = pygame.image.load(path)
        return image

def initialization():
        # pygame initialization
        pygame.init()
        # set screen dimention
        (width, height) = (800, 500)
        screen = pygame.display.set_mode((width, height))
        # set title
        pygame.display.set_caption('CPEN442 Group 2 Project Prototype')
        clearScreen()
        # start display
        pygame.display.flip()

# set closed car door image
def setClosedCarDoorImg():
        image = get_image('/Users/nico/Desktop/CPEN442-Prototype/DoorClosed.png')
        image = pygame.transform.scale(image, (240, 180))
        screen.blit(image, (20, 150))

# set opened car door image
def setOpenedCarDoorImg():
        image = get_image('/Users/nico/Desktop/CPEN442-Prototype/DoorOpen.png')
        image = pygame.transform.scale(image, (240, 180))
        screen.blit(image, (20, 150))

# set key fob
def setFobImg(x, y):
        image = get_image('/Users/nico/Desktop/CPEN442-Prototype/Fob.png')
        image = pygame.transform.scale(image, (128, 128))
        screen.blit(image, (x, y))

# set attacker
def setAttackerImg(x, y):
        image = get_image('/Users/nico/Desktop/CPEN442-Prototype/Thief.png')
        image = pygame.transform.scale(image, (128, 128))
        screen.blit(image, (x, y))

# set house
def drawHouse():
        pygame.draw.rect(screen, (0,0,0), (640, 170, 148, 148), width=5)
        pygame.draw.polygon(screen, (0,0,0), [(630,170), (798,170), (714,120)], width=5)

# clear screen
def clearScreen():
        # set background colour
        background_colour = pygame.color.Color(255,255,255)
        screen.fill(background_colour)

# update display
def updateDisplay():
        pygame.display.update()

# car door unlocked!
def bingo():
        setOpenedCarDoorImg()
        updateDisplay()
        time.sleep(3)
        setClosedCarDoorImg()
        updateDisplay()
        time.sleep(3)

# a mouse click event has occured, change images position and try authenticate
def changePositions():
        # clicking fob image on the right
        if pos[0] >= 640 and pos[0] <= 788 and pos[1] >= 170 and pos[1] <= 318:
            clearScreen()
            setClosedCarDoorImg()
            drawHouse()
            setAttackerImg(400, 372)
            setFobImg(300, 180)
            # try authenticate here
            tryAuthenticate()
            updateDisplay()

        # clicking fob image on the left
        elif pos[0] >= 300 and pos[0] <= 428 and pos[1] >= 180 and pos[1] <= 308:
            clearScreen()
            setClosedCarDoorImg()
            drawHouse()
            setAttackerImg(400, 372)
            setFobImg(650, 180)
            # try authenticate here
            tryAuthenticate()
            updateDisplay()

        # clicking attacker image at the bottom
        elif pos[0] >= 400 and pos[0] <= 528 and pos[1] >= 372 and pos[1] <= 500:
            clearScreen()
            setClosedCarDoorImg()
            drawHouse()
            setAttackerImg(400, 180)
            setFobImg(650, 180)
            # try authenticate here
            tryAuthenticate()
            updateDisplay()

        # clicking attacker image at the top (650, 180, 128, 128)
        elif pos[0] >= 400 and pos[0] <= 528 and pos[1] >= 180 and pos[1] <= 308:
            clearScreen()
            setClosedCarDoorImg()
            drawHouse()
            setAttackerImg(400, 372)
            setFobImg(650, 180)
            # try authenticate here
            tryAuthenticate()
            updateDisplay()

# try authenticate
def tryAuthenticate():
        # communication protocol here
        print("Protocol")


initialization()
setClosedCarDoorImg()
setFobImg(650, 180)
drawHouse()
setAttackerImg(400, 372)
updateDisplay()

# wait until users wanna quit the program
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      # exit program
      pygame.quit()

    # mouse click
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      changePositions()
