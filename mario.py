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
from copy import copy
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
bglimitH = screenH - bgH

def draw_floor():
    for floor in floor_list:
        temp_rect = copy(floor)
        temp_rect.x += bg_x_pos # glue # actually minus
        pygame.draw.rect(screen, (0,0,0), temp_rect)
        
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

def colliderect_on_bg(bully, victim):
    
    temp_victim = copy(victim) 
    temp_victim.x += bg_x_pos 
    return bully.colliderect(temp_victim)

def check_collisonsx():
    global mario_rect
    global hit_box_list
    global mario_count
    """
    enemy: False is victim is not enemy, True if victim is enemy
    - Therefore we can let mario dies if he hits an enemy instead of wall
    """
    for hit_box in hit_box_list:
        # 896 -> 896 -> 896 
        # 0 -> 100 -> 200 -> 500 

        temp_hit_box = copy(hit_box)
        temp_hit_box.x += bg_x_pos
        if mario_rect.colliderect(temp_hit_box):
            if abs(mario_rect.top - temp_hit_box.bottom) > 5:
                if moving_right == True:
                    mario_rect.x = temp_hit_box.left - mario_rect.w
                    mario_count = 4     
                elif moving_left == True:
                    mario_rect.x = temp_hit_box.right
                    mario_count = 4

def check_collisonsy():
    global mario_rect
    global hit_box_list 
    global jump
    global default_on_ground_y
    global on_ground
    """
    enemy: False is victim is not enemy, True if victim is enemy
    - Therefore we can let mario dies if he hits an enemy instead of wall
    """
    for hit_box in hit_box_list:
        temp_hit_box = copy(hit_box)
        temp_hit_box.x += bg_x_pos
        if mario_rect.colliderect(temp_hit_box):
            if velocity_y > 0: #mario is jumping up 
                print(mario_rect.top)
                jump = False
            elif velocity_y < 0: #mario is jumping down 
                default_on_ground_y = temp_hit_box.top
                mario_rect.bottom =  default_on_ground_y 
                on_ground = True
        elif mario_rect.bottom > default_on_ground_y:
            on_ground = False


while True:
    
    draw_floor()
    screen.blit(bg, (bg_x_pos,0))                  #paint background
    # ### NAZ's CODES ###
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         sys.exit()

    #     if event.type == pygame.KEYDOWN:     #user pressed a key      
    #         if event.key == pygame.K_d:      #user pressed the D key
    #             marioWalkR = True
    #         if event.key == pygame.K_a:      #user pressed the A key
    #             marioWalkL = True
    #         if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
    #             mario_rect.y -= mario_speed
    #         if event.key == pygame.K_s or event.key == pygame.K_DOWN:
    #             mario_rect.y += mario_speed
        
    #     if event.type == pygame.KEYUP:       #user released a key
    #         if event.key == pygame.K_d:      #user released the D key
    #             marioWalkR = False
    #         if event.key == pygame.K_a:      #user released the A key
    #             marioWalkL = False

    ########################################

    ### BEN's codes ### 
    # goomba move
    if (goomba_alive == True) and (abs(goomba_hitbox.x - abs(bg_x_pos)) <= 800):
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
    if (mario_rect.colliderect(goomba_hitbox) and (on_ground == False)) == True:
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

    ### EEJOY's CODES ###
     # Brick 1

    if draw_brick1:
        draw_on_bg(brick, rect = brick_rect1)

    if collidepoint_on_bg(mario_rect, brick_rect1.midbottom):
        draw_brick1 = False
    
    # Brick 2
    if draw_brick2:
        draw_on_bg(brick, rect = brick_rect2)

    if collidepoint_on_bg(mario_rect, brick_rect2.midbottom):
        draw_brick2 = False
    
    # Brick 3
    if draw_brick3:
        draw_on_bg(brick, rect = brick_rect3)

    if collidepoint_on_bg(mario_rect, brick_rect3.midbottom):
        draw_brick3 = False

    # Brick 4
    if draw_brick4:
        draw_on_bg(brick, rect = brick_rect4)

    if collidepoint_on_bg(mario_rect, brick_rect4.midbottom):
        draw_brick4 = False

    # Brick 5
    if draw_brick5:
        draw_on_bg(brick, rect = brick_rect5)

    if collidepoint_on_bg(mario_rect, brick_rect5.midbottom):
        draw_brick5 = False

    # Brick 6
    if draw_brick6:
        draw_on_bg(brick, rect = brick_rect6)

    if collidepoint_on_bg(mario_rect, brick_rect6.midbottom):
        draw_brick6 = False

    # Brick 7
    if draw_brick7:
        draw_on_bg(brick, rect = brick_rect7)

    if collidepoint_on_bg(mario_rect, brick_rect7.midbottom):
        draw_brick7 = False

    # Brick 8
    if draw_brick8:
        draw_on_bg(brick, rect = brick_rect8)

    if collidepoint_on_bg(mario_rect, brick_rect8.midbottom):
        draw_brick8 = False
    
    # Brick 9
    if draw_brick9:
        draw_on_bg(brick, rect = brick_rect9)

    if collidepoint_on_bg(mario_rect, brick_rect9.midbottom):
        draw_brick9 = False

    # Brick 10
    if draw_brick10:
        draw_on_bg(brick, rect = brick_rect10)

    if collidepoint_on_bg(mario_rect, brick_rect10.midbottom):
        draw_brick10 = False
    
    # Brick 11
    if draw_brick11:
        draw_on_bg(brick, rect = brick_rect11)

    if collidepoint_on_bg(mario_rect, brick_rect11.midbottom):
        draw_brick11 = False

    # Brick 12
    if draw_brick12:
        draw_on_bg(brick, rect = brick_rect12)

    if collidepoint_on_bg(mario_rect, brick_rect12.midbottom):
        draw_brick12 = False
    
    # Brick 13
    if draw_brick13:
        draw_on_bg(brick, rect = brick_rect13)

    if collidepoint_on_bg(mario_rect, brick_rect13.midbottom):
        draw_brick13 = False

    # Brick 14
    if draw_brick14:
        draw_on_bg(brick, rect = brick_rect14)

    if collidepoint_on_bg(mario_rect, brick_rect14.midbottom):
        draw_brick14 = False

    # Brick 15
    if draw_brick15:
        draw_on_bg(brick, rect = brick_rect15)

    if collidepoint_on_bg(mario_rect, brick_rect15.midbottom):
        draw_brick15 = False

    # Brick 16
    if draw_brick16:
        draw_on_bg(brick, rect = brick_rect16)

    if collidepoint_on_bg(mario_rect, brick_rect16.midbottom):
        draw_brick16 = False

    # Brick 17
    if draw_brick17:
        draw_on_bg(brick, rect = brick_rect17)

    if collidepoint_on_bg(mario_rect, brick_rect17.midbottom):
        draw_brick17 = False

    # Brick 18
    if draw_brick18:
        draw_on_bg(brick, rect = brick_rect18)

    if collidepoint_on_bg(mario_rect, brick_rect18.midbottom):
        draw_brick18 = False

    # Brick 19
    if draw_brick19:
        draw_on_bg(brick, rect = brick_rect19)

    if collidepoint_on_bg(mario_rect, brick_rect19.midbottom):
        draw_brick19 = False

    # Brick 20
    if draw_brick20:
        draw_on_bg(brick, rect = brick_rect20)

    if collidepoint_on_bg(mario_rect, brick_rect20.midbottom):
        draw_brick20 = False

    # Brick 21
    if draw_brick21:
        draw_on_bg(brick, rect = brick_rect21)

    if collidepoint_on_bg(mario_rect, brick_rect21.midbottom):
        draw_brick21 = False

    # Brick 22
    if draw_brick22:
        draw_on_bg(brick, rect = brick_rect22)

    if collidepoint_on_bg(mario_rect, brick_rect22.midbottom):
        draw_brick22 = False

    # Brick 23
    if draw_brick23:
        draw_on_bg(brick, rect = brick_rect23)

    if collidepoint_on_bg(mario_rect, brick_rect23.midbottom):
        draw_brick23 = False

    # Brick 24
    if draw_brick24:
        draw_on_bg(brick, rect = brick_rect24)

    if collidepoint_on_bg(mario_rect, brick_rect24.midbottom):
        draw_brick24 = False

    # Brick 25
    if draw_brick25:
        draw_on_bg(brick, rect = brick_rect25)

    if collidepoint_on_bg(mario_rect, brick_rect25.midbottom):
        draw_brick25 = False

    # Brick 26
    if draw_brick26:
        draw_on_bg(brick, rect = brick_rect26)

    if collidepoint_on_bg(mario_rect, brick_rect26.midbottom):
        draw_brick26 = False

    # Brick 27
    if draw_brick27:
        draw_on_bg(brick, rect = brick_rect27)

    if collidepoint_on_bg(mario_rect, brick_rect27.midbottom):
        draw_brick27 = False

    # Brick 28
    if draw_brick28:
        draw_on_bg(brick, rect = brick_rect28)

    if collidepoint_on_bg(mario_rect, brick_rect28.midbottom):
        draw_brick28 = False

    # Brick 29
    if draw_brick29:
        draw_on_bg(brick, rect = brick_rect29)

    if collidepoint_on_bg(mario_rect, brick_rect29.midbottom):
        draw_brick29 = False
    # COIN FLASH 
    coin_count += 0.1
    if coin_count >= 3:
        coin_count = 0 
    # # Draw bricks
    # draw_on_bg(brick, (640, 272))
    # draw_on_bg(brick, (704, 272))
    # draw_on_bg(brick, (768, 272))
    # draw_on_bg(brick, (2462, 272))
    # draw_on_bg(brick, (2511, 272))
    # draw_on_bg(brick, (2559, 144))
    # draw_on_bg(brick, (2591, 144))
    # draw_on_bg(brick, (2624, 144))
    # draw_on_bg(brick, (2656, 144))
    # draw_on_bg(brick, (2688, 144))
    # draw_on_bg(brick, (2656, 144))
    # draw_on_bg(brick, (2720, 144))
    # # draw_on_bg(brick, (752, 144))
    # draw_on_bg(brick, (2784, 144))
    # draw_on_bg(brick, (2911, 144))
    # draw_on_bg(brick, (2943, 144))
    # draw_on_bg(brick, (2975, 144))
    # draw_on_bg(brick, rect = coin_brick_rect) # Coin brick
    # draw_on_bg(brick, (3199, 272))
    # draw_on_bg(brick, rect = star_brick_rect) # Star brick
    # draw_on_bg(brick, (3774, 272))
    # draw_on_bg(brick, (3871, 144))
    # draw_on_bg(brick, (3903, 144))
    # draw_on_bg(brick, (3935, 144))
    # draw_on_bg(brick, (4095, 144))
    # draw_on_bg(brick, (4159, 144))
    # draw_on_bg(brick, (4192, 144))
    # draw_on_bg(brick, (4127, 272))
    # draw_on_bg(brick, (4159, 272))
    # draw_on_bg(brick, (5374, 272))
    # draw_on_bg(brick, (5407, 272))
    # draw_on_bg(brick, (5471, 272))
    
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
        count_star_rect += 0.1
        if count_star_rect >= 3:
            count_star_rect = 0

        # Let the star bounces in the region where x-coor >3000 & <4200, and y-coor >304 & <368
        if star_rect.y <= 334:
            vy = 5
        
        if star_rect.y >= 368:
            vy = -5

        if star_rect.x <= 3000:
            vx = 4

        # if star_rect.x >= 4200:
        #     vx = -4

        y_vel = vy
        x_vel = vx

        star_rect.y += y_vel
        star_rect.x += x_vel

    if star_rect.top >= star_brick_rect.bottom and colliderect_on_bg(mario_rect, star_rect):
        draw_star = False

    # Draw coin box
    draw_on_bg(question_block[int(coin_count)], rect = question_rect1)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect2)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect3)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect4)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect5)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect6)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect7)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect8)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect9)

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
    draw_on_bg(question_block[int(coin_count)], rect = question_rect10)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect11)
    draw_on_bg(question_block[int(coin_count)], rect = question_rect12)

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
        if red_mushroom_rect1.midbottom[1] >= question_rect10.midtop[1]:
            red_mushroom_rect1.y -= 1

    if draw_empty_brick10:
        draw_on_bg(empty_brick, rect = question_rect10)
    

    if (red_mushroom_rect1.bottom <= question_rect10.top) and (colliderect_on_bg(mario_rect, red_mushroom_rect1)):
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
    ### RAJA's ###
    #mario move and jump
    # while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:         
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: 
                moving_right = True
                moving_left = False  
            if event.key == pygame.K_a or event.key == pygame.K_LEFT: 
                moving_left = True
                moving_right = False
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if on_ground == True: #makes it run only once 
                    on_ground = False
                    jump = True

        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                moving_right = False
                mario_count = 4
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                moving_left = False
                mario_count = 4
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                jump = False
    
    if jump == True:
        mario_count = 5
        velocity_y = 6
        if mario_rect.top > bglimitH:
            mario_rect.y -= velocity_y #goes up 
            if mario_rect.bottom <= (default_on_ground_y - JUMP_HEIGHT):
                mario_rect.bottom = default_on_ground_y - JUMP_HEIGHT
                jump = False
        else:
            jump = False
    else:
        velocity_y = -6
        mario_rect.y -= velocity_y #goes down
        if on_ground:
            if moving_left or moving_right == True:
                mario_count += 0.09
                if mario_count >= 4:
                    mario_count = 0 
            else:
                mario_count = 4

    check_collisonsy() 

    if moving_right == True:
        direction = facing_right 
        if bg_x_pos > bgLimit:                   #logic to stop when limit is reached
            if mario_rect.x < (575 - marioW):     #limit mario's movement to before the mid section
                mario_rect.x += velocity_x
            else:
                bg_x_pos -= velocity_x          #after reaching the middle, background will move

    if moving_left == True:
        direction = facing_left
        if mario_rect.x >= 0:
            mario_rect.x -= velocity_x
    check_collisonsx()

    if on_ground == False:
        mario_count = 5
    

    if direction == -1:
        screen.blit(marioflip[int(mario_count)], (mario_rect.x,mario_rect.y))
    elif direction == 0:
        screen.blit(animation_list[4], (mario_rect.x,mario_rect.y))
    else:
        screen.blit(animation_list[int(mario_count)], (mario_rect.x,mario_rect.y))
    ####################################################
    pygame.display.update()                        #update screen
    clock.tick(60)                                 #limit our game to 60 fps no matter what

