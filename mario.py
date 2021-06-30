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
start_ticks= pygame.time.get_ticks() # Use to countdown 

# function to draw the floors, total of 4 floors 
def draw_floor():
    for floor in floor_list:
        temp_rect = copy(floor)
        temp_rect.x += bg_x_pos # glue # actually minus
        pygame.draw.rect(screen, (0,0,0), temp_rect)
        
# function to blit pictures (not rect) that sticks to the background 
# without this function everything will move with mario 
def draw_on_bg(pic, xy = (0,0), rect=False):
    # use this function instead of blit if you want 
    # to blit an image that sticks to the screen
    # instead of moving along with mario 
    if rect == False:
        screen.blit(pic,(bg_x_pos + xy[0], xy[1]))
    else:
        screen.blit(pic, (bg_x_pos + rect.x, rect.y))
    
# detect collidepoint while the rect is stick to the background
# without this function the rects will just move along with mario
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

# detect colliderect while the rect is stick to the background
# without this function the rects will just move along with mario
def colliderect_on_bg(bully, victim):
    
    temp_victim = copy(victim) 
    temp_victim.x += bg_x_pos 
    return bully.colliderect(temp_victim)

# check mario's horizontal collision, if detected, stop mario from moving
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

# check mario's vertical collision, if detected, stop mario from going up or down
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
                jump = False
            elif velocity_y < 0: #mario is jumping down 
                default_on_ground_y = temp_hit_box.top
                mario_rect.bottom =  default_on_ground_y 
                on_ground = True
        elif mario_rect.bottom > default_on_ground_y:
            on_ground = False

#### #### #### #### #### EEJOY's #### #### #### #### #### ####
def draw_brick_rect(brick_rect):
    if collidepoint_on_bg(mario_rect, brick_rect.midbottom):
        remove_brick_list.append(brick_rect) #Reverse, works
        remove_brick_rect(brick_rect) #remove the rect
    
    if brick_rect not in remove_brick_list: #don't draw if it's collided
        draw_on_bg(brick, rect = brick_rect)

def remove_brick_rect(brick_rect): #remove rects so it doesn't collide anymore
    for rect in hit_box_list:
        if rect == brick_rect:
            hit_box_list.remove(brick_rect)

def draw_empty_brick_rect(question_rect):
    if question_rect in empty_brick_list:
        draw_on_bg(empty_brick, rect = question_rect)

def draw_coin_rect(question_rect, coin_rect):
    if collidepoint_on_bg(mario_rect, question_rect.midbottom):
        remove_coin_list.append(coin_rect)
        empty_brick_list.append(question_rect)
        
    if coin_rect in remove_coin_list:
        draw_on_bg(coin, rect = coin_rect)
        coin_jump(coin_rect, question_rect)

    draw_empty_brick_rect(question_rect) 

def coin_jump(coin_rect, question_rect):
    global m
    global v

    if not coin_rect.y > question_rect.y:
        F = (1/2) * m * (v ** 2)
        coin_rect.y -= F
        v -= 0.2
        if v < 0:
            m = -1
    else:
        remove_coin_rect(coin_rect)
        m = 1
        v = 5

def remove_coin_rect(coin_rect):
    for coin in remove_coin_list:
        if coin == coin_rect:
            remove_coin_list.remove(coin_rect)
    
def draw_mushroom_rect(question_rect, red_mushroom_rect):
    if collidepoint_on_bg(mario_rect, question_rect.midbottom):
        remove_mushroom_list.append(red_mushroom_rect)
        empty_brick_list.append(question_rect)
        
    if red_mushroom_rect in remove_mushroom_list:
        draw_on_bg(red_mushroom, rect = red_mushroom_rect)
        mushroom_rise(red_mushroom_rect, question_rect)

    remove_mushroom_rect(red_mushroom_rect)
    draw_empty_brick_rect(question_rect)

def mushroom_rise(red_mushroom_rect, question_rect):
    if ((red_mushroom_rect.midbottom[1] >= question_rect10.midtop[1]) and 
       not(red_mushroom_rect.bottom <= question_rect.top)):
        red_mushroom_rect.y -= 1

def remove_mushroom_rect(red_mushroom_rect):
    if colliderect_on_bg(mario_rect, red_mushroom_rect):
        for mushroom in remove_mushroom_list:
            if mushroom == red_mushroom_rect:
                remove_mushroom_list.remove(red_mushroom_rect)

#### #### #### #### #### EEJOY's end #### #### #### #### #### ####

def update_score(X):
    # everytime did something call this function 
    """
    X - value to be added, an integer
    """
    global score_value 
    score_value += int(X)

def update_coins():
    # everytime hit a coin call this function
    global coins_value
    coins_value += 1

# update_time not needed

def game_reset():
    # one of the reasons why you want to use class
    # too many global when it comes to things like this
    global bg_x_pos
    global mario_size
    global mario_state
    global mario_dead
    global mario_died_one_time
    global draw_coin
    global draw_star
    global start_time
    global goomba_alive
    global on_ground
    global score_value
    global coins_value
    global time_value
    global lives_value
    global main_theme_play
    global main_theme_fastvers
    global invincible__music
    
    bg_x_pos = 0
    mario_size = 0
    mario_state = 0
    start_time = 0
    mario_dead = False
    mario_died_one_time = False
    draw_coin = False
    draw_star = False
    goomba_alive = True
    on_ground = True
    score_value = 0
    coins_value = 0
    time_value = 400
    lives_value = 3
    main_theme_play = False
    main_theme_fastvers = False
    invincible__music = False

def update_lives():
    # call this funcion everytime mario dies 
    # UNFINISHED
    global lives_value
    lives_value -= 1

    if lives_value == 0:
        pygame.display.update()
        screen.fill((0,0,0))
        screen.blit(gameoverText,gameoverText_rect)
        game_over_song.play(loops=0,maxtime=0,fade_ms=0)

    else:
        game_reset()
    
while True:
    
    draw_floor() #draw the floor before the BG 
    screen.blit(bg, (bg_x_pos,0)) #draw BG 

    # ~ Mario dead logic 
    if mario_dead == False:
        # timer to decrease the 400 times 
        # in Mario, 1 sec is 0.6 sec in real life 
        seconds=(pygame.time.get_ticks()-start_ticks)/600
        if (time_value - int(seconds)) <= 0:
            mario_dead = True

        if (mario_rect.y > 448):
            mario_dead = True
            
    else:
        # these are the things that only have to 
        # happen ONE TIME after mario died
        mario_dead_sound.play(loops=0,maxtime=0,fade_ms=0)

        if mario_died_one_time == False:
            mario_died_x = mario_rect.x
            mario_died_y = mario_rect.y
            mario_died_one_time = True
            update_lives()

        # ~ Let Mario jumps when he dies 
        if mario_died_y <= 272:
            mario_dead_velo = 3
        mario_died_y += mario_dead_velo


    # ~ Render Top texts 
    screen.blit(score_font, (50,0))
    score_value_font = mario_font.render(str(score_value), False, WHITE)
    # need to place it in the middle of the above font 
    # logics below 
    # get the half width of the above font, then plus its original X location, then minus 
    # value's font width divide by 2, you can get the exact center.. 
    exact_center = score_font.get_width()/2 + 50 - score_value_font.get_width()/2
    screen.blit(score_value_font, (exact_center, 30))

    screen.blit(coins_font, (250,0))
    coins_value_font = mario_font.render(str(coins_value), False, WHITE)
    exact_center = coins_font.get_width()/2 + 250 - coins_value_font.get_width()/2
    screen.blit(coins_value_font, (exact_center, 30))

    screen.blit(world_font, (450,0))
    world_value_font = mario_font.render(world_value, False, WHITE)
    exact_center = world_font.get_width()/2 + 450 - world_value_font.get_width()/2
    screen.blit(world_value_font, (exact_center, 30))

    screen.blit(time_font, (650,0))
    time_value_font = mario_font.render(str(time_value-int(seconds)), False, WHITE)
    exact_center = time_font.get_width()/2 + 650 - time_value_font.get_width()/2
    screen.blit(time_value_font, (exact_center, 30))

    screen.blit(lives_font, (850,0))
    lives_value_font = mario_font.render(str(lives_value), False, WHITE)
    exact_center = lives_font.get_width()/2 + 850 - lives_value_font.get_width()/2
    screen.blit(lives_value_font, (exact_center, 30))

    #### #### #### #### #### BEN's #### #### #### #### #### ####
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
    print(mario_rect.bottom)
    if (colliderect_on_bg(mario_rect, goomba_hitbox) and (on_ground == False)) == True:
        goomba_alive = False
    elif (colliderect_on_bg(mario_rect, goomba_hitbox) and goomba_alive) == True:
        mario_dead = True

    #### #### #### #### #### BEN's end #### #### #### #### #### ####

    #### #### #### #### #### YUN SION's #### #### #### #### #### ####
    draw_on_bg(titleBanner, (37.5, 75)) 
    draw_on_bg(copywrite, (200, 250))
    #### #### #### #### #### YUN SION's #### #### #### #### #### ####

    #### #### #### #### #### EEJOY's #### #### #### #### #### ####
    # Draw the bricks and remove when collision is detected
    draw_brick_rect(brick_rect1)
    draw_brick_rect(brick_rect2)
    draw_brick_rect(brick_rect3)
    draw_brick_rect(brick_rect4)
    draw_brick_rect(brick_rect5)
    draw_brick_rect(brick_rect6)
    draw_brick_rect(brick_rect7)
    draw_brick_rect(brick_rect8)
    draw_brick_rect(brick_rect9)
    draw_brick_rect(brick_rect10)
    draw_brick_rect(brick_rect11)
    draw_brick_rect(brick_rect12)
    draw_brick_rect(brick_rect13)
    draw_brick_rect(brick_rect14)
    draw_brick_rect(brick_rect15)
    draw_brick_rect(brick_rect16)
    draw_brick_rect(brick_rect17)
    draw_brick_rect(brick_rect18)
    draw_brick_rect(brick_rect19)
    draw_brick_rect(brick_rect20)
    draw_brick_rect(brick_rect21)
    draw_brick_rect(brick_rect22)
    draw_brick_rect(brick_rect23)
    draw_brick_rect(brick_rect24)
    draw_brick_rect(brick_rect25)
    draw_brick_rect(brick_rect26)
    draw_brick_rect(brick_rect27)
    draw_brick_rect(brick_rect28)
    draw_brick_rect(brick_rect29)
    
    draw_on_bg(brick, rect = coin_brick_rect) # Coin brick
    draw_on_bg(brick, rect = star_brick_rect) # Star brick

    # Coin brick - draw coin
    if collidepoint_on_bg(mario_rect, coin_brick_rect.midbottom):
        count_coin += 1

        # Only draw coin for the first time of collision
        if count_coin == 1:
            draw_coin = True
            m = 1
            v = 5
            
    if draw_coin:
        draw_on_bg(coin, rect = coin_rect0)

        # Let the coin jump
        F = (1/2) * m * (v ** 2) 
        coin_rect0.y -= F
        v -= 0.1
        if v < 0:
            m = -1

    if coin_rect0.y > coin_brick_rect.y:
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

    # Question block flash
    question_count += 0.1
    if question_count >= 3:
        question_count = 0 

    # Draw coin box
    draw_on_bg(question_block[int(question_count)], rect = question_rect1)
    draw_on_bg(question_block[int(question_count)], rect = question_rect2)
    draw_on_bg(question_block[int(question_count)], rect = question_rect3)
    draw_on_bg(question_block[int(question_count)], rect = question_rect4)
    draw_on_bg(question_block[int(question_count)], rect = question_rect5)
    draw_on_bg(question_block[int(question_count)], rect = question_rect6)
    draw_on_bg(question_block[int(question_count)], rect = question_rect7)
    draw_on_bg(question_block[int(question_count)], rect = question_rect8)
    draw_on_bg(question_block[int(question_count)], rect = question_rect9)

    draw_coin_rect(question_rect1, coin_rect1)
    draw_coin_rect(question_rect2, coin_rect2)
    draw_coin_rect(question_rect3, coin_rect3)
    draw_coin_rect(question_rect4, coin_rect4)
    draw_coin_rect(question_rect5, coin_rect5)
    draw_coin_rect(question_rect6, coin_rect6)
    draw_coin_rect(question_rect7, coin_rect7)
    draw_coin_rect(question_rect8, coin_rect8)
    draw_coin_rect(question_rect9, coin_rect9)

    # Draw mushroom box
    draw_on_bg(question_block[int(question_count)], rect = question_rect10)
    draw_on_bg(question_block[int(question_count)], rect = question_rect11)
    draw_on_bg(question_block[int(question_count)], rect = question_rect12)

    draw_mushroom_rect(question_rect10, red_mushroom_rect1)
    draw_mushroom_rect(question_rect11, red_mushroom_rect2)
    draw_mushroom_rect(question_rect12, red_mushroom_rect3)

    #### #### #### #### #### EEJOY's end #### #### #### #### #### ####

    #### #### #### #### #### RAJA's #### #### #### #### #### ####
    
    # ~ MOVE and JUMP 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if mario_dead == False:
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

        # ~ DISABLE MOVE/JUMP 
            if event.type == pygame.KEYUP:  
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    moving_right = False
                    mario_count = 4
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    moving_left = False
                    mario_count = 4
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    jump = False
        if mario_dead == True:
            moving_right = False
            moving_left = False
            mario_count = 4
            jump = False

    # ~ JUMP's logic 
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
    
    check_collisonsy() # check vertical collision immediately so mario don't jump thru blocks, or go thru floors.

    # WALK's logics
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

    check_collisonsx() # check horizontal collision immediately so mario don't walk past rects like Pipes

    # ~ JUMP and WALK animation 
    if mario_dead == False:
        if on_ground == False:
            mario_count = 5

        if direction == -1:
            screen.blit(marioflip[int(mario_count)], (mario_rect.x,mario_rect.y))
        elif direction == 0:
            screen.blit(animation_list[4], (mario_rect.x,mario_rect.y))
        else:
            screen.blit(animation_list[int(mario_count)], (mario_rect.x,mario_rect.y))
    else:
        screen.blit(mario_died_pic,(mario_died_x, mario_died_y))
    #### #### #### #### #### RAJA's end #### #### #### #### #### ####

    pygame.display.update()  #update screen
    clock.tick(60)  #limit our game to 60 fps no matter what
