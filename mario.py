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

def draw_on_bg(pic, xy = (0,0), rect = False):
    # use this function instead of blit if you want 
    # to blit an image that sticks to the screen
    # instead of moving along with mario 
    if rect == False:
        screen.blit(pic, (bg_x_pos + xy[0], xy[1]))
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

# *****
def colliderect_on_bg(bully, victim):
    victim.left += bg_x_pos
    return bully.colliderect(victim)

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
    draw_on_bg(brick, rect = coin_brick_rect) # Coin brick
    draw_on_bg(brick, rect = star_brick_rect) # Star brick

    # def collide_brick(mario_rect, brick, brick_rect, draw_brick):
    #     if collidepoint_on_bg(mario_rect, brick_rect.midbottom):
    #         draw_brick = False
    #     if draw_brick:
    #         draw_on_bg(brick, rect = brick_rect)
    
    # collide_brick(mario_rect, brick, brick_rect1, draw_brick1)
    
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
        draw_coin = False

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

        # Let the star rises slowly
        # if star_rect.midbottom != star_brick_rect.midtop:
        #     star_rect.y -= 1

        # x_vel = 1
        # m = 1
        # v = 5
        # y_vel = (1/2) * m * (v**2)

        if star_rect.y <= 304:
            vy = 2
        
        if star_rect.y >= 368:
            vy = -2

        if star_rect.x >= 4200:
            vx = -2

        if star_rect.x <= 3000:
            vx = 2

        y_vel = vy
        x_vel = vx

        star_rect.y += y_vel
        star_rect.x += x_vel

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

    # def collide_coin(mario_rect, question_rect, count_coin, draw_empty_brick, draw_coin, coin, coin_rect):
    #     if collidepoint_on_bg(mario_rect, question_rect.midbottom):
    #         count_coin1 += 1

    #         # Only draw coin for the first time of collision
    #         if count_coin == 1:
    #             draw_empty_brick = True
    #             draw_coin = True
    #             m = 1
    #             v = 5

    #     if draw_coin:
    #         draw_on_bg(coin, rect = coin_rect)

    #         # Let the coin jump
    #         F = (1/2) * m * (v ** 2)
    #         coin_rect.y -= F
    #         v -= 0.2
    #         if v < 0:
    #             m = -1

    #     if draw_empty_brick:
    #         draw_on_bg(empty_brick, rect = question_rect)

    #     if coin_rect.y > question_rect.y:
    #         draw_coin = False


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

    # ******
    if colliderect_on_bg(mario_rect, red_mushroom_rect1):
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
    
    # Let star bounces
    # floor = pygame.draw.rect(screen, )

    ####################################################
    pygame.display.update()                        #update screen
    clock.tick(60)                                 #limit our game to 60 fps no matter what
