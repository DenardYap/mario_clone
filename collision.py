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
screen = pygame.display.set_mode((1000, 448))

# I forgot to mention 'Clock'
# the 'clock' instance help us to control the FPS
# see below - clock.tick(60) makes the fps to be 60 
clock = pygame.time.Clock()

# import images & animation here
# Tips: The bricks (floor) is 48px height

# Import background
bg = pygame.image.load("static_images/background.png")

# Import mario
mario = pygame.image.load("static_images/mario.png")
mario_rect = mario.get_rect(topleft = (40, 368))

# Import brick
brick = pygame.image.load("static_images/brick.png")
coin_brick_rect = brick.get_rect(topleft = (3007, 272))
star_brick_rect = brick.get_rect(topleft = (3231, 272))

# Import coin
coin = pygame.image.load("static_images/coin.png")
coin_rect = coin.get_rect()

# Import mushroom
red_mushroom = pygame.image.load("static_images/red_mushroom.png")
red_mushroom_rect = red_mushroom.get_rect()

# Import question block
question_block = []
question_block.append(pygame.image.load("animate_images/question_block0.png"))
question_block.append(pygame.image.load("animate_images/question_block1.png"))
question_block.append(pygame.image.load("animate_images/question_block2.png"))

# Coin box
question_rect1 = question_block[0].get_rect(topleft = (511, 272))
question_rect2 = question_block[0].get_rect(topleft = (736, 272))
question_rect3 = question_block[0].get_rect(topleft = (703, 144))
question_rect4 = question_block[0].get_rect(topleft = (3007, 144))
question_rect5 = question_block[0].get_rect(topleft = (3391, 272))
question_rect6 = question_block[0].get_rect(topleft = (3486, 272))
question_rect7 = question_block[0].get_rect(topleft = (3582, 272))
question_rect8 = question_block[0].get_rect(topleft = (4127, 144))
question_rect9 = question_block[0].get_rect(topleft = (5439, 272))

# Mushroom box
question_rect10 = question_block[0].get_rect(topleft = (672, 272))
question_rect11 = question_block[0].get_rect(topleft = (2494, 272))
question_rect12 = question_block[0].get_rect(topleft = (3486, 144))

# Import star
star = []
star.append(pygame.image.load("animate_images/star0.png"))
star.append(pygame.image.load("animate_images/star1.png"))
star.append(pygame.image.load("animate_images/star2.png"))
star.append(pygame.image.load("animate_images/star3.png"))
star_rect = star[0].get_rect(topleft = (3231, 240))

# Setup
mario_speed = 5.0
count = 0

draw_coin = False
draw_star = False
count_star = 0

draw_coin1 = False
draw_coin2 = False
draw_coin3 = False
draw_coin4 = False
draw_coin5 = False
draw_coin6 = False
draw_coin7 = False
draw_coin8 = False
draw_coin9 = False

draw_mushroom1 = False
draw_mushroom2 = False
draw_mushroom3 = False

while True:
    # Index for question box
    count += 0.2
    if count >= 3:
        count = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                mario_rect.x += mario_speed
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                mario_rect.x -= mario_speed
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                mario_rect.y -= mario_speed
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                mario_rect.y += mario_speed
    
    # Draw background and mario
    screen.blit(bg, (0, 0))
    screen.blit(mario, mario_rect)

    # Draw bricks
    screen.blit(brick, (640, 272))
    screen.blit(brick, (704, 272))
    screen.blit(brick, (768, 272))
    screen.blit(brick, (2462, 272))
    screen.blit(brick, (2511, 272))
    screen.blit(brick, (2559, 144))
    screen.blit(brick, (2591, 144))
    screen.blit(brick, (2624, 144))
    screen.blit(brick, (2656, 144))
    screen.blit(brick, (2688, 144))
    screen.blit(brick, (2656, 144))
    screen.blit(brick, (2720, 144))
    screen.blit(brick, (2752, 144))
    screen.blit(brick, (2784, 144))
    screen.blit(brick, (2911, 144))
    screen.blit(brick, (2943, 144))
    screen.blit(brick, (2975, 144))
    screen.blit(brick, coin_brick_rect) # Coin brick
    screen.blit(brick, (3199, 272))
    screen.blit(brick, star_brick_rect) # Star brick
    screen.blit(brick, (3774, 272))
    screen.blit(brick, (3871, 144))
    screen.blit(brick, (3903, 144))
    screen.blit(brick, (3935, 144))
    screen.blit(brick, (4095, 144))
    screen.blit(brick, (4159, 144))
    screen.blit(brick, (4192, 144))
    screen.blit(brick, (4127, 272))
    screen.blit(brick, (4159, 272))
    screen.blit(brick, (5374, 272))
    screen.blit(brick, (5407, 272))
    screen.blit(brick, (5471, 272))

    # Coin brick - draw coin
    if mario_rect.collidepoint(coin_brick_rect.midbottom):
        draw_coin = True
        
    if mario_rect.colliderect(coin_rect):
        draw_coin = False

    if draw_coin:
        coin_rect.midbottom = coin_brick_rect.midtop
        screen.blit(coin, coin_rect)

    # Star brick - draw star
    if mario_rect.collidepoint(star_brick_rect.midbottom):
        draw_star = True

    if mario_rect.colliderect(star_rect):
        draw_star = False

    if draw_star:
        star_rect.midbottom = star_brick_rect.midtop
        screen.blit(star[int(count_star)], star_rect)

        count_star += 1
        if count_star >= 1:
            count = 0

    # Draw coin box
    screen.blit(question_block[int(count)], question_rect1)
    screen.blit(question_block[int(count)], question_rect2)
    screen.blit(question_block[int(count)], question_rect3)
    screen.blit(question_block[int(count)], question_rect4)
    screen.blit(question_block[int(count)], question_rect5)
    screen.blit(question_block[int(count)], question_rect6)
    screen.blit(question_block[int(count)], question_rect7)
    screen.blit(question_block[int(count)], question_rect8)
    screen.blit(question_block[int(count)], question_rect9)

    # Coin 1
    if mario_rect.collidepoint(question_rect1.midbottom):
        draw_coin1 = True

    if mario_rect.colliderect(coin_rect):
        draw_coin1 = False

    if draw_coin1:
        coin_rect.midbottom = question_rect1.midtop
        screen.blit(coin, coin_rect)

    # Coin 2
    if mario_rect.collidepoint(question_rect2.midbottom):
        draw_coin2 = True
        
    if mario_rect.colliderect(coin_rect):
        draw_coin2 = False

    if draw_coin2:
        coin_rect.midbottom = question_rect2.midtop
        screen.blit(coin, coin_rect)

    # Coin 3
    if mario_rect.collidepoint(question_rect3.midbottom):
        draw_coin3 = True
        
    if mario_rect.colliderect(coin_rect):
        draw_coin3 = False

    if draw_coin3:
        coin_rect.midbottom = question_rect3.midtop
        screen.blit(coin, coin_rect)

    # Coin 4
    if mario_rect.collidepoint(question_rect4.midbottom):
        draw_coin4 = True
        
    if mario_rect.colliderect(coin_rect):
        draw_coin4 = False

    if draw_coin4:
        coin_rect.midbottom = question_rect4.midtop
        screen.blit(coin, coin_rect)

    # Coin 5  
    if mario_rect.collidepoint(question_rect5.midbottom):
        draw_coin5 = True
        
    if mario_rect.colliderect(coin_rect):
        draw_coin5 = False
    
    if draw_coin5:
        coin_rect.midbottom = question_rect5.midtop
        screen.blit(coin, coin_rect)

    # Coin 6  
    if mario_rect.collidepoint(question_rect6.midbottom):
        draw_coin6 = True
    
    if mario_rect.colliderect(coin_rect):
        draw_coin6 = False

    if draw_coin6:    
        coin_rect.midbottom = question_rect6.midtop
        screen.blit(coin, coin_rect)

    # Coin 7
    if mario_rect.collidepoint(question_rect7.midbottom):
        draw_coin7 = True

    if mario_rect.colliderect(coin_rect):
        draw_coin7 = False

    if draw_coin7:
        coin_rect.midbottom = question_rect7.midtop
        screen.blit(coin, coin_rect)

    # Coin 8
    if mario_rect.collidepoint(question_rect8.midbottom):
        draw_coin8 = True
        
    if mario_rect.colliderect(coin_rect):
        draw_coin8 = False

    if draw_coin8:
        coin_rect.midbottom = question_rect8.midtop
        screen.blit(coin, coin_rect)

    # Coin 9
    if mario_rect.collidepoint(question_rect9.midbottom):
        draw_coin9 = True
        
    if mario_rect.colliderect(coin_rect):
        draw_coin9 = False

    if draw_coin9:
        coin_rect.midbottom = question_rect9.midtop
        screen.blit(coin, coin_rect)

    # Draw mushroom box
    screen.blit(question_block[int(count)], question_rect10)
    screen.blit(question_block[int(count)], question_rect11)
    screen.blit(question_block[int(count)], question_rect12)

    # Mushroom 1
    if mario_rect.collidepoint(question_rect10.midbottom):
        draw_mushroom1 = True

    if mario_rect.colliderect(coin_rect):
        draw_mushroom1 = False

    if draw_mushroom1:
        red_mushroom_rect.midbottom = question_rect10.midtop
        screen.blit(red_mushroom, red_mushroom_rect)
    
    # Mushroom 2
    if mario_rect.collidepoint(question_rect11.midbottom):
        draw_mushroom2 = True
        
    if mario_rect.colliderect(coin_rect):
        draw_mushroom2 = False

    if draw_mushroom2:
        red_mushroom_rect.midbottom = question_rect11.midtop
        screen.blit(red_mushroom, red_mushroom_rect)

    # Mushroom 3
    if mario_rect.collidepoint(question_rect12.midbottom):
        draw_mushroom3 = True

    if mario_rect.colliderect(coin_rect):
        draw_mushroom3 = False

    if draw_mushroom3:
        red_mushroom_rect.midbottom = question_rect12.midtop
        screen.blit(red_mushroom, red_mushroom_rect)

    
    

    pygame.display.update()
    clock.tick(60) #limit our game to 60 fps no matter what
