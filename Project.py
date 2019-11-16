import sys
import pygame
import os
import time

screen = pygame.display.set_mode((0, 0))
pos = (0, 0)
# initially positions of key and thief
key_home = True
car_thief = False

# grabbing the image to return
def get_image(path):
        image = pygame.image.load(path)
        return image

def initialization():
        global screen
        global key_home
        global car_thief
        # pygame initialization
        pygame.init()
        # set screen dimention
        (width, height) = (800, 500)
        screen = pygame.display.set_mode((width, height))
        # set title
        pygame.display.set_caption('CPEN442 Group 2 Project Prototype')
        # start display
        pygame.display.flip()

        resetAll()

def resetAll():
        global screen
        global key_home
        global car_thief

        # set all images and global variables
        clearScreen()
        setClosedCarDoorImg()
        setFobImg(650, 180)
        drawHouse()
        setAttackerImg(400, 372)
        key_home = True
        car_thief = False
        updateDisplay()

# set closed car door image
def setClosedCarDoorImg():
        global screen
        image = get_image('/Users/nico/Desktop/CPEN442-Prototype/DoorClosed.png')
        image = pygame.transform.scale(image, (240, 180))
        screen.blit(image, (20, 150))

# set opened car door image
def setOpenedCarDoorImg():
        global screen
        image = get_image('/Users/nico/Desktop/CPEN442-Prototype/DoorOpen.png')
        image = pygame.transform.scale(image, (240, 180))
        screen.blit(image, (20, 150))

# set key fob
def setFobImg(x, y):
        global screen
        image = get_image('/Users/nico/Desktop/CPEN442-Prototype/Fob.png')
        image = pygame.transform.scale(image, (128, 128))
        screen.blit(image, (x, y))

# set attacker
def setAttackerImg(x, y):
        global screen
        image = get_image('/Users/nico/Desktop/CPEN442-Prototype/Thief.png')
        image = pygame.transform.scale(image, (128, 128))
        screen.blit(image, (x, y))

# set house
def drawHouse():
        pygame.draw.rect(screen, (0,0,0), (640, 170, 148, 148), width=5)
        pygame.draw.polygon(screen, (0,0,0), [(630,170), (798,170), (714,120)], width=5)

# clear screen
def clearScreen():
        global screen
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
        global key_home
        global car_thief
        # clicking fob image on the right
        if pos[0] >= 640 and pos[0] <= 788 and pos[1] >= 170 and pos[1] <= 318:
            key_home = False
            clearScreen()
            setClosedCarDoorImg()
            drawHouse()
            setAttackerImg(400, 372)
            setFobImg(300, 180)
            updateDisplay()
            # try authenticate here
            tryAuthenticate()

        # clicking fob image on the left
        elif pos[0] >= 300 and pos[0] <= 428 and pos[1] >= 180 and pos[1] <= 308:
            key_home = True
            clearScreen()
            setClosedCarDoorImg()
            drawHouse()
            setAttackerImg(400, 372)
            setFobImg(650, 180)
            updateDisplay()
            # try authenticate here
            tryAuthenticate()

        # clicking attacker image at the bottom
        elif pos[0] >= 400 and pos[0] <= 528 and pos[1] >= 372 and pos[1] <= 500:
            car_thief = True
            clearScreen()
            setClosedCarDoorImg()
            drawHouse()
            setAttackerImg(400, 180)
            setFobImg(650, 180)
            updateDisplay()
            # try authenticate here
            tryAuthenticate()

        # clicking attacker image at the top
        elif pos[0] >= 400 and pos[0] <= 528 and pos[1] >= 180 and pos[1] <= 308:
            car_thief = False
            clearScreen()
            setClosedCarDoorImg()
            drawHouse()
            setAttackerImg(400, 372)
            setFobImg(650, 180)
            updateDisplay()
            # try authenticate here
            tryAuthenticate()

# try authenticate
def tryAuthenticate():
        global key_home
        global car_thief
        # key is home and thief is not there
        if key_home == True and car_thief == False:
                print("No signals detected by car")
        
        # key is home and thief is there (Relay attack)
        elif key_home == True and car_thief == True:
                print("Signals detected by car, starting authentication process...")

        # key is not home and thief is not there (car owner unlocking)
        elif key_home == False and car_thief == False:
                print("Signals detected by car, starting authentication process...")

        else:
                print("Car thief is arrested")
                resetAll()


initialization()

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
