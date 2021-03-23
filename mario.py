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
screen = pygame.display.set_mode((1000,448))

# I forgot to mention 'Clock'
# the 'clock' instance help us to control the FPS
# see below - clock.tick(60) makes the fps to be 60 
clock = pygame.time.Clock()

# import images & animation here
# Tips: The bricks (floor) is 48px height



# goomba
goomba_alive = True
goomba_size = (32, 32)
goomba_animation_i = 0
goomba_animation_list = []
goomba_animation_list.append(pygame.image.load("./animate_images/goomba0.png"))
goomba_animation_list.append(pygame.image.load("./animate_images/goomba1.png"))
for (i, image) in enumerate(goomba_animation_list):
    goomba_animation_list[i] = pygame.transform.scale(goomba_animation_list[i], goomba_size)
goomba_hitbox = goomba_animation_list[0].get_rect(topleft = (700, 448-48-32))
goomba_death_ani = pygame.transform.scale(pygame.image.load("./static_images/goomba_died.png"), (32, 16))

# import sounds here



# import fonts here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # get mario events




    # goomba
    # goomba move
    if goomba_alive == True:
        goomba_hitbox.x -= 2

    # goomba animation
    goomba_animation_i += 1
    if goomba_animation_i == 20:
        goomba_animation_i = 0

    # goomba render
    if goomba_alive == True:
        screen.blit(goomba_animation_list[int(goomba_animation_i/10)], goomba_hitbox)
    else:
        screen.blit(goomba_death_ani, (goomba_hitbox.x, (goomba_hitbox.y + int(goomba_hitbox.height / 2))))

    # check collsion
    if (mario_hitbox.colliderect(goomba_hitbox) and goomba_alive) == True:
        print("Game over!")
    elif (mario_hitbox.collidepoint((goomba_hitbox.x, goomba_hitbox.y-1)) or mario_hitbox.collidepoint((goomba_hitbox.x + goomba_hitbox.width, goomba_hitbox.y-1)) or mario_hitbox.collidepoint(goomba_hitbox.x + (int(goomba_hitbox.width / 2)), goomba_hitbox.y-1)) == True:
        goomba_alive = False


    pygame.display.update()
    clock.tick(60) #limit our game to 60 fps no matter what
