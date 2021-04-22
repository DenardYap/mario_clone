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
from resources import * 
from constants import * 

#initializing pygame
pygame.init()

# 1000px width and 448px height
screen = pygame.display.set_mode((screenW,screenH))

clock = pygame.time.Clock()

#variables
bgLimit = screenW - bgW

def draw_on_bg(pic, xy = (0,0), rect=False):
    # use this function instead of blit if you want 
    # to blit an image that sticks to the screen
    # instead of moving along with mario 
    if rect == False:
        screen.blit(pic,(bg_x_pos + xy[0], xy[1]))
    else:
        screen.blit(pic, (bg_x_pos + rect.x, rect.y))
    
def collidepoint_on_bg(bully, victim):
    # use this function instead of collidepoint
    # as we need to detect rects that are sticked
    # to the background image
    """
    bully: a rect (mario)
    victim: a rect (kooba, goomba, etc?) with any reference point (midbottom, center, etc)
            reference point must be a tuple of (x,y)
    """
    return bully.collidepoint((bg_x_pos + victim[0], victim[1]))

while True:
        
    screen.blit(bg, (bg_x_pos,0))                  #paint background
    ### NAZ's CODES ###
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:     #user pressed a key      
            if event.key == pygame.K_d:      #user pressed the D key
                marioWalkR = True
            if event.key == pygame.K_a:      #user pressed the A key
                marioWalkL = True
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                mario_rect.y -= mario_speed
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                mario_rect.y += mario_speed
        
        if event.type == pygame.KEYUP:       #user released a key
            if event.key == pygame.K_d:      #user released the D key
                marioWalkR = False
            if event.key == pygame.K_a:      #user released the A key
                marioWalkL = False

    #Mario walk right logic       
    if marioWalkR == True:
        if bg_x_pos > bgLimit:                   #logic to stop when limit is reached
            if mario_rect.x < (575 - marioW):     #limit mario's movement to before the mid section
                mario_rect.x += mario_speed   
            else:
                bg_x_pos -= mario_speed           #after reaching the middle, background will move

    if marioWalkL == True:
        if mario_rect.x > 0:                        #make sure he does not go off screen
            mario_rect.x -= mario_speed
    ########################################

    ### BEN's codes ### 
    # goomba move
    if goomba_alive == True:
        goomba_hitbox.x -= 1

    # goomba animation
    goomba_animation_i += 0.1
    if goomba_animation_i >= 2:
        goomba_animation_i = 0

    # goomba render
    if goomba_alive == True:
        draw_on_bg(goomba_animation_list[int(goomba_animation_i)], rect = goomba_hitbox)
    else:
        draw_on_bg(goomba_death_ani, (goomba_hitbox.x, (goomba_hitbox.y + int(goomba_hitbox.height / 2))))
        # add a delay to dissapear the dead goomba 
    # check collsion
    if (mario_rect.collidepoint((goomba_hitbox.x + 4, goomba_hitbox.y - 1)) or 
    mario_rect.collidepoint((goomba_hitbox.x + goomba_hitbox.width - 4, goomba_hitbox.y - 1)) or 
    mario_rect.collidepoint(goomba_hitbox.x + (int(goomba_hitbox.width / 2)), goomba_hitbox.y - 1)) == True:
        goomba_alive = False
    elif (mario_rect.colliderect(goomba_hitbox) and goomba_alive) == True:
        print("Game over!")
        sys.exit()

    ########################################

    ### YUN SION's codes ###
    draw_on_bg(titleBanner, (37.5, 45)) 
    draw_on_bg(copywrite, (200, 220))

    # Gameover scene # 
    # when mario dies, play this #
    # screen.fill((0,0,0))
    # screen.blit(gameoverText,gameoverText_rect)
    # game_over_sound.play(loops=0,maxtime=0,fade_ms=0)
    ########################

    screen.blit(mario, mario_rect)  #paint mario

    ### EEJOY's CODES ###
    # COIN FLASH 
    count += 0.1
    if count >= 3:
        count = 0 
    # Draw bricks
    draw_on_bg(brick, (640, 272))
    draw_on_bg(brick, (704, 272))
    draw_on_bg(brick, (768, 272))
    draw_on_bg(brick, (2462, 272))
    draw_on_bg(brick, (2511, 272))
    draw_on_bg(brick, (2559, 144))
    draw_on_bg(brick, (2591, 144))
    draw_on_bg(brick, (2624, 144))
    draw_on_bg(brick, (2656, 144))
    draw_on_bg(brick, (2688, 144))
    draw_on_bg(brick, (2656, 144))
    draw_on_bg(brick, (2720, 144))
    # draw_on_bg(brick, (752, 144))
    draw_on_bg(brick, (2784, 144))
    draw_on_bg(brick, (2911, 144))
    draw_on_bg(brick, (2943, 144))
    draw_on_bg(brick, (2975, 144))
    draw_on_bg(brick, rect = coin_brick_rect) # Coin brick
    draw_on_bg(brick, (3199, 272))
    draw_on_bg(brick, rect = star_brick_rect) # Star brick
    draw_on_bg(brick, (3774, 272))
    draw_on_bg(brick, (3871, 144))
    draw_on_bg(brick, (3903, 144))
    draw_on_bg(brick, (3935, 144))
    draw_on_bg(brick, (4095, 144))
    draw_on_bg(brick, (4159, 144))
    draw_on_bg(brick, (4192, 144))
    draw_on_bg(brick, (4127, 272))
    draw_on_bg(brick, (4159, 272))
    draw_on_bg(brick, (5374, 272))
    draw_on_bg(brick, (5407, 272))
    draw_on_bg(brick, (5471, 272))
    
    # Coin brick - draw coin
    if collidepoint_on_bg(mario_rect, coin_brick_rect.midbottom):
        count_coin += 1

        # Only draw coin for the first time of collision
        if count_coin == 1:
            draw_coin = True
            m = 1
            v = 5
            
    if draw_coin:
        draw_on_bg(coin, rect = coin_rect)

        # Let the coin jump
        F = (1/2) * m * (v ** 2) 
        # GJ
        coin_rect.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if coin_rect.y > coin_brick_rect.y:
        draw_coin1 = False

    # Star brick - draw star
    if collidepoint_on_bg(mario_rect, star_brick_rect.midbottom):
        count_star += 1

        # Only draw coin for the first time of collision
        if count_star == 1:
            draw_star = True

    if draw_star:
        draw_on_bg(star[int(count_star_rect)], rect = star_rect)

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
    draw_on_bg(question_block[int(count)], rect = question_rect1)
    draw_on_bg(question_block[int(count)], rect = question_rect2)
    draw_on_bg(question_block[int(count)], rect = question_rect3)
    draw_on_bg(question_block[int(count)], rect = question_rect4)
    draw_on_bg(question_block[int(count)], rect = question_rect5)
    draw_on_bg(question_block[int(count)], rect = question_rect6)
    draw_on_bg(question_block[int(count)], rect = question_rect7)
    draw_on_bg(question_block[int(count)], rect = question_rect8)
    draw_on_bg(question_block[int(count)], rect = question_rect9)

    # Coin 1
    if collidepoint_on_bg(mario_rect, question_rect1.midbottom):
        count_coin1 += 1

        # Only draw coin for the first time of collision
        if count_coin1 == 1:
            draw_empty_brick1 = True
            draw_coin1 = True
            m = 1
            v = 5

    if draw_coin1:
        draw_on_bg(coin, rect = coin_rect1)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect1.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick1:
        draw_on_bg(empty_brick, rect = question_rect1)

    if coin_rect1.y > question_rect1.y:
        draw_coin1 = False

    # Coin 2
    if collidepoint_on_bg(mario_rect, question_rect2.midbottom):
        count_coin2 += 1
        # Only draw coin for the first time of collision
        if count_coin2 == 1:
            draw_empty_brick2 = True
            draw_coin2 = True
            m = 1
            v = 5

    if draw_coin2:
        draw_on_bg(coin, rect = coin_rect2)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect2.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick2:
        draw_on_bg(empty_brick, rect = question_rect2)

    if coin_rect2.y > question_rect2.y:
        draw_coin2 = False
        
    # Coin 3
    if collidepoint_on_bg(mario_rect, question_rect3.midbottom):
        count_coin3 += 1

        # Only draw coin for the first time of collision
        if count_coin3 == 1:
            draw_empty_brick3 = True
            draw_coin3 = True
            m = 1
            v = 5

    if draw_coin3:
        draw_on_bg(coin, rect = coin_rect3)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect3.y -= F
        v -= 0.2
        if v < 0:
            m = -1
    
    if draw_empty_brick3:
        draw_on_bg(empty_brick, rect = question_rect3)

    if coin_rect3.y > question_rect3.y:
        draw_coin3 = False

    # Coin 4
    if collidepoint_on_bg(mario_rect, question_rect4.midbottom):
        count_coin4 += 1

        # Only draw coin for the first time of collision
        if count_coin4 == 1:
            draw_empty_brick4 = True
            draw_coin4 = True
            m = 1
            v = 5
            
    if draw_coin4:
        draw_on_bg(coin, rect = coin_rect4)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect4.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick4:
        draw_on_bg(empty_brick, rect = question_rect4)

    if coin_rect4.y > question_rect4.y:
        draw_coin4 = False

    # Coin 5  
    if collidepoint_on_bg(mario_rect, question_rect5.midbottom):
        count_coin5 += 1

        # Only draw coin for the first time of collision
        if count_coin5 == 1:
            draw_empty_brick5 = True
            draw_coin5 = True
            m = 1
            v = 5
            
    if draw_coin5:
        draw_on_bg(coin, rect = coin_rect5)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect5.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick5:
        draw_on_bg(empty_brick, rect = question_rect5)

    if coin_rect5.y > question_rect5.y:
        draw_coin5 = False

    # Coin 6  
    if collidepoint_on_bg(mario_rect, question_rect6.midbottom):
        count_coin6 += 1

        # Only draw coin for the first time of collision
        if count_coin6 == 1:
            draw_empty_brick6 = True
            draw_coin6 = True
            m = 1
            v = 5
            
    if draw_coin6:
        draw_on_bg(coin, rect = coin_rect6)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect6.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick6:
        draw_on_bg(empty_brick, rect = question_rect6)

    if coin_rect6.y > question_rect6.y:
        draw_coin6 = False

    # Coin 7
    if collidepoint_on_bg(mario_rect, question_rect7.midbottom):
        count_coin7 += 1

        # Only draw coin for the first time of collision
        if count_coin7 == 1:
            draw_empty_brick7 = True
            draw_coin7 = True
            m = 1
            v = 5
            
    if draw_coin7:
        draw_on_bg(coin, rect = coin_rect7)
        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect7.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick7:
        draw_on_bg(empty_brick, rect = question_rect7)

    if coin_rect7.y > question_rect7.y:
        draw_coin7 = False

    # Coin 8
    if collidepoint_on_bg(mario_rect, question_rect8.midbottom):
        count_coin8 += 1

        # Only draw coin for the first time of collision
        if count_coin8 == 1:
            draw_empty_brick8 = True
            draw_coin8 = True
            m = 1
            v = 5
            
    if draw_coin8:
        draw_on_bg(coin, rect = coin_rect8)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect8.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick8:
        draw_on_bg(empty_brick, rect = question_rect8)

    if coin_rect8.y > question_rect8.y:
        draw_coin8 = False

    # Coin 9
    if collidepoint_on_bg(mario_rect, question_rect9.midbottom):
        count_coin9 += 1

        # Only draw coin for the first time of collision
        if count_coin9 == 1:
            draw_empty_brick9 = True
            draw_coin9 = True
            m = 1
            v = 5
            
    if draw_coin9:
        draw_on_bg(coin, rect = coin_rect9)

        # Let the coin jump
        F = (1/2) * m * (v ** 2)
        coin_rect9.y -= F
        v -= 0.2
        if v < 0:
            m = -1

    if draw_empty_brick9:
        draw_on_bg(empty_brick, rect = question_rect9)

    if coin_rect9.y > question_rect9.y:
        draw_coin9 = False

    # Draw mushroom box
    draw_on_bg(question_block[int(count)], rect = question_rect10)
    draw_on_bg(question_block[int(count)], rect = question_rect11)
    draw_on_bg(question_block[int(count)], rect = question_rect12)

    # Mushroom 1
    if collidepoint_on_bg(mario_rect, question_rect10.midbottom):
        count_mushroom1 += 1

        # Only draw coin for the first time of collision
        if count_mushroom1 == 1:
            draw_empty_brick10 = True
            draw_mushroom1 = True

    if draw_mushroom1:
        draw_on_bg(red_mushroom, rect = red_mushroom_rect1)

        # Let the mushroom rise slowly
        if red_mushroom_rect1.midbottom != question_rect10.midtop:
            red_mushroom_rect1.y -= 3

    if draw_empty_brick10:
        draw_on_bg(empty_brick, rect = question_rect10)

    if mario_rect.colliderect(red_mushroom_rect1):
        draw_mushroom1 = False
    
    # Mushroom 2
    if collidepoint_on_bg(mario_rect, question_rect11.midbottom):
        count_mushroom2 += 1

        # Only draw coin for the first time of collision
        if count_mushroom2 == 1:
            draw_empty_brick11 = True
            draw_mushroom2 = True

    if draw_mushroom2:
        draw_on_bg(red_mushroom, rect = red_mushroom_rect2)

        # Let the mushroom rise slowly
        if red_mushroom_rect2.midbottom != question_rect11.midtop:
            red_mushroom_rect2.y -= 3

    if draw_empty_brick11:
        draw_on_bg(empty_brick, rect = question_rect11)

    if mario_rect.colliderect(red_mushroom_rect2):
        draw_mushroom2 = False

    # Mushroom 3
    if collidepoint_on_bg(mario_rect, question_rect12.midbottom):
        count_mushroom3 += 1

        # Only draw coin for the first time of collision
        if count_mushroom3 == 1:
            draw_empty_brick12 = True
            draw_mushroom3 = True

    if draw_mushroom3:
        draw_on_bg(red_mushroom, rect = red_mushroom_rect3)

        # Let the mushroom rise slowly
        if red_mushroom_rect3.midbottom != question_rect12.midtop:
            red_mushroom_rect3.y -= 3

    if draw_empty_brick12:
        draw_on_bg(empty_brick, rect = question_rect12)

    if mario_rect.colliderect(red_mushroom_rect3):
        draw_mushroom3 = False
    
    ####################################################
    pygame.display.update()                        #update screen
    clock.tick(60)                                 #limit our game to 60 fps no matter what
