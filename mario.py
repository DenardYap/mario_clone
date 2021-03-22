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
# create a screen instance/object with 
# 1000px width and 448px height
screen = pygame.display.set_mode((1200,800))

# I forgot to mention 'Clock'
# the 'clock' instance help us to control the FPS
# see below - clock.tick(60) makes the fps to be 60 
clock = pygame.time.Clock()

# import images & animation here
# Tips: The bricks (floor) is 48px height

goomba_size = (32, 32)
goomba_animation_i = 0
goomba_animation_list = []
goomba_animation_list.append(pygame.image.load("./static_images/goomba-1.png"))
goomba_animation_list.append(pygame.image.load("./static_images/goomba-2.png"))
for (i, image) in enumerate(goomba_animation_list):
    goomba_animation_list[i] = pygame.transform.scale(goomba_animation_list[i], goomba_size)

# import sounds here



# import fonts here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    goomba_animation_i += 1
    if goomba_animation_i == 20:
        goomba_animation_i = 0
    screen.blit(goomba_animation_list[int(goomba_animation_i/10)], (0, 752))


    pygame.display.update()
    clock.tick(60) #limit our game to 60 fps no matter what
