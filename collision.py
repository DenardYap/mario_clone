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
coin_rect = coin.get_rect(midtop = (3023, 272))
coin_rect1 = coin.get_rect(midtop = (527, 272))
coin_rect2 = coin.get_rect(midtop = (752, 272))
coin_rect3 = coin.get_rect(midtop = (719, 144))
coin_rect4 = coin.get_rect(midtop = (3023, 144))
coin_rect5 = coin.get_rect(midtop = (3407, 272))
coin_rect6 = coin.get_rect(midtop = (3502, 272))
coin_rect7 = coin.get_rect(midtop = (3598, 272))
coin_rect8 = coin.get_rect(midtop = (4143, 144))
coin_rect9 = coin.get_rect(midtop = (5455, 272))

# Import mushroom
red_mushroom = pygame.image.load("static_images/red_mushroom.png")
red_mushroom_rect1 = red_mushroom.get_rect(topleft = (672, 270))
red_mushroom_rect2 = red_mushroom.get_rect(topleft = (2494, 270))
red_mushroom_rect3 = red_mushroom.get_rect(topleft = (3486, 142))

# Import empty brick
empty_brick = pygame.image.load("static_images/empty_brick.png")

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
star_rect = star[0].get_rect(topleft = (3231, 270))

# Setup
mario_speed = 5.0
count = 0

draw_coin = False
draw_star = False
count_coin = 0
count_star = 0
count_star_rect = 0

draw_coin1 = False
draw_coin2 = False
draw_coin3 = False
draw_coin4 = False
draw_coin5 = False
draw_coin6 = False
draw_coin7 = False
draw_coin8 = False
draw_coin9 = False

count_coin1 = 0
count_coin2 = 0
count_coin3 = 0
count_coin4 = 0
count_coin5 = 0
count_coin6 = 0
count_coin7 = 0
count_coin8 = 0
count_coin9 = 0

draw_mushroom1 = False
draw_mushroom2 = False
draw_mushroom3 = False

count_mushroom1 = 0
count_mushroom2 = 0
count_mushroom3 = 0

draw_empty_brick1 = False
draw_empty_brick2 = False
draw_empty_brick3 = False
draw_empty_brick4 = False
draw_empty_brick5 = False
draw_empty_brick6 = False
draw_empty_brick7 = False
draw_empty_brick8 = False
draw_empty_brick9 = False
draw_empty_brick10 = False
draw_empty_brick11 = False
draw_empty_brick12 = False


while True:
    # Index for question box
    count += 0.1
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
        count_coin += 1

        # Only draw coin for the first time of collision
        if count_coin == 1:
            draw_coin = True
            m = 1
            v = 5
            
    if draw_coin:
        screen.blit(coin, coin_rect)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect1.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if coin_rect.y > coin_brick_rect.y:
        draw_coin1 = False

    # Star brick - draw star
    if mario_rect.collidepoint(star_brick_rect.midbottom):
        count_star += 1

        # Only draw coin for the first time of collision
        if count_star == 1:
            draw_star = True

    if draw_star:
        screen.blit(star[int(count_star)], star_rect)

        # Index of star
        count_star_rect += 0.2
        if count_star_rect >= 3:
            count_star_rect = 0

        # Let the mushroom rise slowly
        if star_rect.midbottom != star_brick_rect.midtop:
            star_rect.y -= 1

    if mario_rect.colliderect(star_rect):
        draw_star = False

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
        count_coin1 += 1

        # Only draw coin for the first time of collision
        if count_coin1 == 1:
            draw_empty_brick1 = True
            draw_coin1 = True
            m = 1
            v = 5

    if draw_coin1:
        screen.blit(coin, coin_rect1)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect1.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick1:
        screen.blit(empty_brick, question_rect1)

    if coin_rect1.y > question_rect1.y:
        draw_coin1 = False

    # Coin 2
    if mario_rect.collidepoint(question_rect2.midbottom):
        count_coin2 += 1

        # Only draw coin for the first time of collision
        if count_coin2 == 1:
            draw_empty_brick2 = True
            draw_coin2 = True
            m = 1
            v = 5

    if draw_coin2:
        screen.blit(coin, coin_rect2)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect2.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick2:
        screen.blit(empty_brick, question_rect2)

    if coin_rect2.y > question_rect2.y:
        draw_coin2 = False
        
    # Coin 3
    if mario_rect.collidepoint(question_rect3.midbottom):
        count_coin3 += 1

        # Only draw coin for the first time of collision
        if count_coin3 == 1:
            draw_empty_brick3 = True
            draw_coin3 = True
            m = 1
            v = 5

    if draw_coin3:
        screen.blit(coin, coin_rect3)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect3.y -= F
        v -= 0.2
        if v < 0:
            m = -1
    
    if draw_empty_brick3:
        screen.blit(empty_brick, question_rect3)

    if coin_rect3.y > question_rect3.y:
        draw_coin3 = False

    # Coin 4
    if mario_rect.collidepoint(question_rect4.midbottom):
        count_coin4 += 1

        # Only draw coin for the first time of collision
        if count_coin4 == 1:
            draw_empty_brick4 = True
            draw_coin4 = True
            m = 1
            v = 5
            
    if draw_coin4:
        screen.blit(coin, coin_rect4)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect4.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick4:
        screen.blit(empty_brick, question_rect4)

    if coin_rect4.y > question_rect4.y:
        draw_coin4 = False

    # Coin 5  
    if mario_rect.collidepoint(question_rect5.midbottom):
        count_coin5 += 1

        # Only draw coin for the first time of collision
        if count_coin5 == 1:
            draw_empty_brick5 = True
            draw_coin5 = True
            m = 1
            v = 5
            
    if draw_coin5:
        screen.blit(coin, coin_rect5)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect5.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick1:
        screen.blit(empty_brick, question_rect5)

    if coin_rect5.y > question_rect5.y:
        draw_coin5 = False

    # Coin 6  
    if mario_rect.collidepoint(question_rect6.midbottom):
        count_coin6 += 1

        # Only draw coin for the first time of collision
        if count_coin6 == 1:
            draw_empty_brick6 = True
            draw_coin6 = True
            m = 1
            v = 5
            
    if draw_coin6:
        screen.blit(coin, coin_rect6)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect6.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick6:
        screen.blit(empty_brick, question_rect6)

    if coin_rect6.y > question_rect6.y:
        draw_coin6 = False

    # Coin 7
    if mario_rect.collidepoint(question_rect7.midbottom):
        count_coin7 += 1

        # Only draw coin for the first time of collision
        if count_coin7 == 1:
            draw_empty_brick7 = True
            draw_coin7 = True
            m = 1
            v = 5
            
    if draw_coin7:
        screen.blit(coin, coin_rect7)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect7.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick7:
        screen.blit(empty_brick, question_rect7)

    if coin_rect7.y > question_rect7.y:
        draw_coin7 = False

    # Coin 8
    if mario_rect.collidepoint(question_rect8.midbottom):
        count_coin8 += 1

        # Only draw coin for the first time of collision
        if count_coin8 == 1:
            draw_empty_brick8 = True
            draw_coin8 = True
            m = 1
            v = 5
            
    if draw_coin8:
        screen.blit(coin, coin_rect8)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect8.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick8:
        screen.blit(empty_brick, question_rect8)

    if coin_rect8.y > question_rect8.y:
        draw_coin8 = False

    # Coin 9
    if mario_rect.collidepoint(question_rect9.midbottom):
        count_coin9 += 1

        # Only draw coin for the first time of collision
        if count_coin9 == 1:
            draw_empty_brick9 = True
            draw_coin9 = True
            m = 1
            v = 5
            
    if draw_coin9:
        screen.blit(coin, coin_rect9)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect9.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick9:
        screen.blit(empty_brick, question_rect9)

    if coin_rect9.y > question_rect9.y:
        draw_coin9 = False

    # Draw mushroom box
    screen.blit(question_block[int(count)], question_rect10)
    screen.blit(question_block[int(count)], question_rect11)
    screen.blit(question_block[int(count)], question_rect12)

    # Mushroom 1
    if mario_rect.collidepoint(question_rect10.midbottom):
        count_mushroom1 += 1

        # Only draw coin for the first time of collision
        if count_mushroom1 == 1:
            draw_empty_brick10 = True
            draw_mushroom1 = True

    if draw_mushroom1:
        screen.blit(red_mushroom, red_mushroom_rect1)

        # Let the mushroom rise slowly
        if red_mushroom_rect1.midbottom != question_rect10.midtop:
            red_mushroom_rect1.y -= 3

    if draw_empty_brick10:
        screen.blit(empty_brick, question_rect10)

    if mario_rect.colliderect(red_mushroom_rect1):
        draw_mushroom1 = False
    
    # Mushroom 2
    if mario_rect.collidepoint(question_rect11.midbottom):
        count_mushroom2 += 1

        # Only draw coin for the first time of collision
        if count_mushroom2 == 1:
            draw_empty_brick11 = True
            draw_mushroom2 = True

    if draw_mushroom2:
        screen.blit(red_mushroom, red_mushroom_rect2)

        # Let the mushroom rise slowly
        if red_mushroom_rect2.midbottom != question_rect11.midtop:
            red_mushroom_rect2.y -= 3

    if draw_empty_brick11:
        screen.blit(empty_brick, question_rect11)

    if mario_rect.colliderect(red_mushroom_rect2):
        draw_mushroom2 = False

    # Mushroom 3
    if mario_rect.collidepoint(question_rect12.midbottom):
        count_mushroom3 += 1

        # Only draw coin for the first time of collision
        if count_mushroom3 == 1:
            draw_empty_brick12 = True
            draw_mushroom3 = True

    if draw_mushroom3:
        screen.blit(red_mushroom, red_mushroom_rect3)

        # Let the mushroom rise slowly
        if red_mushroom_rect3.midbottom != question_rect12.midtop:
            red_mushroom_rect3.y -= 3

    if draw_empty_brick12:
        screen.blit(empty_brick, question_rect12)

    if mario_rect.colliderect(red_mushroom_rect3):
        draw_mushroom3 = False

    
    

    pygame.display.update()
    clock.tick(60) #limit our game to 60 fps no matter what
