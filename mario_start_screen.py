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

pygame.init()
screen=pygame.display.set_mode((1000,448))
clock = pygame.time.Clock()

# import images & animation here
# Tips: The bricks (floor) is 48px height
startBackground = pygame.image.load(r'static_images/background.png')
titleBanner = pygame.image.load(r'static_images/title.png')
mario = pygame.image.load(r'static_images/mario.png')

# import sounds here

# import fonts here
pygame.font.init()
font = pygame.font.Font(r'fonts/mario_font.ttf', 24)
copywrite = font.render("©1985 Nintendo", False ,(255,255,0))

while True:

    #start screen
    screen.blit(startBackground, (0,0))
    screen.blit(titleBanner, (337.5,45)) 
    screen.blit(mario, (150,368)) 
    screen.blit(copywrite, (500, 220))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    clock.tick(60) #limit our game to 60 fps no matter what
