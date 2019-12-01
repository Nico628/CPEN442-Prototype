import sys
import pygame
import os
import time
import threading
import nacl.signing
import random

screen = pygame.display.set_mode((0, 0))
pos = (0, 0)
# initially positions of key and thief
key_home = True
car_thief = False
timeout = 1
car_done = False
key_done = False
car_msg = None
key_msg = None

# create digital signatures for car
car_private_key = nacl.signing.SigningKey.generate()
car_public_key = car_private_key.verify_key

# create digital signatures for key
fob_private_key = nacl.signing.SigningKey.generate()
fob_public_key = fob_private_key.verify_key

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

# try authenticate and print
def tryAuthenticate():
        global key_home
        global car_thief
        global key_done
        global car_done

        # key is home and thief is not there
        if key_home == True and car_thief == False:
                setClosedCarDoorImg()
                updateDisplay()
                print("Handle not touched...")
                print("\n")
        
        # key is home and thief is there (Relay attack)
        elif key_home == True and car_thief == True:
                print("\nCar: Handle touched, starting authentication process...")

                thread1 = keyThread(1, "Thread-Key", )
                thread2 = carThread(2, "Thread-Car", )

                thread1.start()
                thread2.start()
                thread1.join()
                thread2.join()
                
                key_done = False
                car_done = False

        # key is not home and thief is not there (car owner unlocking)
        elif key_home == False and car_thief == False:
                print("\nCar: Handle touched, starting authentication process...")

                thread1 = keyThread(1, "Thread-Key", )
                thread2 = carThread(2, "Thread-Car", )

                thread1.start()
                thread2.start()
                thread1.join()
                thread2.join()

                key_done = False
                car_done = False

        else:
                setClosedCarDoorImg()
                updateDisplay()
                print("Car thief is arrested")
                print("\n")
                resetAll()

class carThread (threading.Thread):
        def __init__(self, threadID, name):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name
        def run(self):
                protocol_car()

class keyThread (threading.Thread):
        def __init__(self, threadID, name):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name
        def run(self):
                protocol_key()



def protocol_key():
        global timeout
        global car_done
        global key_done
        global car_msg
        global key_msg
        global car_public_key
        global fob_private_key

        while car_done == False:
                pass

        if car_thief == True:
                time.sleep(timeout*2)
        
        # verify car msg
        try:
                car_public_key.verify(car_msg)
                print("Key: Car message verified...")
        except:
                print("Key: Car message NOT verified...")
                return

        # set car msg as key msg
        key_msg = fob_private_key.sign(car_msg.message)
        print("Key: Signed and sent a message to car...\n")

        if car_thief == True:
                time.sleep(timeout*2)

        # set key msg prepared to done
        key_done = True



def protocol_car():
        global timeout
        global car_done
        global key_done
        global car_msg
        global key_msg
        global car_private_key
        global fob_public_key

        # set a random number as car msg
        random_number = random.randint(0, sys.maxsize)
        car_msg = car_private_key.sign(random_number.to_bytes(20, byteorder='big'))

        # set car msg prepared to done
        car_done = True

        start_time = time.time()

        print("Car: Signed and sent a message to key fob...Setting timeout duration for response...\n")

        while time.time() - start_time <= 4*timeout and key_done == False:
                pass

        if key_done == False:
                # failed authentication
                setClosedCarDoorImg()
                updateDisplay()

                print("Car: Timed out...Please try again...")
                print("\n")
        else:
                print("Car: Received a signed message within timeout window...Verifying message...")
                # verify msg
                try:
                        fob_public_key.verify(key_msg)
                        print("Car: Key message verified...Unlocking...")
                        print("\n")
                        bingo()
                except:
                        print("Car: Key message NOT verified...\n")



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
