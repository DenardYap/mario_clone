"""
Project: Python + Game
Lead: Bernard Yap
Team Members: Benjamin Goh, Nazrin Nazarudin, Yun Sion, Luke Leh, Lim Eejoy, Guan Zhou, Tarun, Raja Darshini
Goal: Clone the original mario game as much as possible!

Credits to justinmeister for all the resources
https://github.com/justinmeister/Mario-Level-1/tree/master/resources/graphics

click on the link below to see the real mario game
https://supermarioplay.com/
"""
import pygame
import sys

#initializing pygame
pygame.init()

# create a screen instance/object with 
# 1000px width and 448px height
screenW = 1000
screenH = 448
screen = pygame.display.set_mode((screenW,screenH))


# I forgot to mention 'Clock'
# the 'clock' instance help us to control the FPS
# see below - clock.tick(60) makes the fps to be 60 
clock = pygame.time.Clock()

# import images & animation here
bg = pygame.image.load("static_images/background.png")
mario = pygame.image.load("static_images/mario.png")

# Tips: The bricks (floor) is 48px height

# import sounds here

# import fonts here

#variables
marioW = 24    #mario width
marioH = 32    #mario height
bg_x_pos = 0   #background position
bgW = 6784     #bacgkround width
bgH = 448      #background height
bgLimit = screenW - bgW
mario_x_pos = 0
mario_y_pos = 368
marioWalkR =  False
marioWalkL = False
marioSpeed = 10



#event
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:     #user pressed a key      
            if event.key == pygame.K_d:      #user pressed the D key
                marioWalkR = True
            if event.key == pygame.K_a:      #user pressed the A key
                marioWalkL = True
        
        if event.type == pygame.KEYUP:       #user released a key
            if event.key == pygame.K_d:      #user released the D key
                marioWalkR = False
            if event.key == pygame.K_a:      #user released the A key
                marioWalkL = False

    #Mario walk right logic       
    if marioWalkR == True:
        if bg_x_pos > bgLimit:                   #logic to stop when limit is reached
            if mario_x_pos < (575 - marioW):     #limit mario's movement to before the mid section
                mario_x_pos += marioSpeed   
            else:
                bg_x_pos -= marioSpeed           #after reaching the middle, background will move




    if marioWalkL == True:
        if mario_x_pos > 0:                        #make sure he does not go off screen
            mario_x_pos -= marioSpeed

    screen.blit(bg, (bg_x_pos,0))                  #paint background
    screen.blit(mario, (mario_x_pos,mario_y_pos))  #paint mario
    pygame.display.update()                        #update screen
    clock.tick(60)                                 #limit our game to 60 fps no matter what

