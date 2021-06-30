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
from pygame import time
from resources import * 
from constants import * 

#initializing pygame
pygame.init()

# 1000px width and 448px height
screen = pygame.display.set_mode((screenW,screenH))
clock = pygame.time.Clock()
time_ticks = pygame.time.get_ticks() # Use to countdown timer on top
TARGET_FPS = 60

# function to draw the floors, total of 4 floors 
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
    global start_time_invincible
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
    start_time_invincible = 0
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
    
# detect colliderect while the rect is stick to the background
# without this function the rects will just move along with mario
def colliderect_on_bg(bully, victim):
    
    temp_victim = copy(victim) 
    temp_victim.x += bg_x_pos 
    return bully.colliderect(temp_victim)

# detect collision from the bottom only while the rect is stick to the background
# without this function the rects will just move along with mario
def colliderect_on_bg_bottom(bully, victim):
    # use this function instead of collidepoint
    # as we need to detect rects that are sticked
    # to the background image
    """
    bully: a rect (mario)
    victim: a rect (kooba, goomba, etc?) with any reference point (midbottom, center, etc)
            reference point must be a tuple of (x,y)
    """
    temp_victim = copy(victim) 
    temp_victim.x += bg_x_pos 
    if bully.colliderect(temp_victim):
        # mario is below the victim and not falling down
        if bully.top <= temp_victim.bottom and mario_m > 0:
            return True
    return False
    # return bully.collidepoint((bg_x_pos + victim[0], victim[1]))

# check mario's horizontal collision, if detected, stop mario from maaaaaoving
def check_collisonsx():
    global mario_rect
    global hit_box_list
    global mario_count
    global acceleration_x
    global velocity_x
    global skied_left
    global skied_right
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
                if moving_left == True or skied_left == False:
                    if skied_right == True:
                        mario_rect.x = temp_hit_box.right
                        mario_count = 4
                if moving_right == True or skied_right == False:
                    if skied_left == True:
                        mario_rect.x = temp_hit_box.left - mario_rect.w
                        mario_count = 4     

# check mario's vertical collision, if detected, stop mario from going up or down
def check_collisonsy():
    global mario_rect
    global hit_box_list 
    global jump
    global default_on_ground_y
    global on_ground
    global velocity_y
    """
    enemy: False is victim is not enemy, True if victim is enemy
    - Therefore we can let mario dies if he hits an enemy instead of wall
    """
    for hit_box in hit_box_list:
        temp_hit_box = copy(hit_box)
        temp_hit_box.x += bg_x_pos
        if mario_rect.colliderect(temp_hit_box):
            if mario_m > 0: #mario is jumping up 
                jump = False
            elif mario_m < 0: #mario is jumping down 
                velocity_y = 6
                default_on_ground_y = temp_hit_box.top
                mario_rect.bottom =  default_on_ground_y 
                on_ground = True
        elif mario_rect.bottom > default_on_ground_y:
            on_ground = False

#### #### #### #### #### EEJOY's #### #### #### #### #### ####

# ~ The names of the functions are pretty intuitive and you 
# ~ can already tell what they do from then func names

def draw_brick_rect(brick_rect):
    global bumping_brick
    global bumping_brick_velo_y
    global bumping_brick_ori_y
    if mario_size != 0 and colliderect_on_bg_bottom(mario_rect, brick_rect):
        if brick_rect not in remove_brick_list:
            brick_smash_sound.play()
        remove_brick_list.append(brick_rect) #Reverse, works
        remove_brick_rect(brick_rect) #remove the rect 
    elif mario_size == 0 and colliderect_on_bg_bottom(mario_rect, brick_rect):
        bump_sound.play()
        bumping_brick = brick_rect
        bumping_brick_ori_y = brick_rect.y
        #move the brick up a bit
    if bumping_brick:
        # fix double bugs
        bumping_brick.y += bumping_brick_velo_y 
        print(bumping_brick.y)
        if bumping_brick.y <= bumping_brick_ori_y - 20:
            bumping_brick_velo_y = 1
        elif bumping_brick.y > bumping_brick_ori_y + 1:
            bumping_brick_velo_y = -1
            bumping_brick.y = bumping_brick_ori_y
            bumping_brick = None
        
    if brick_rect not in remove_brick_list: #don't draw if it's collided
        draw_on_bg(brick, rect = brick_rect)

def remove_brick_rect(brick_rect): #remove rects so it doesn't collide anymore
    for rect in hit_box_list:
        if rect == brick_rect:
            # convert from tuple to list so it becomes mutable
            debris_list["DEBRIS"].append(brick_rect)
            debris_list["Y"].append(debris_vy)
            debris_list["BL"].append([brick_rect.bottomleft[0], brick_rect.bottomleft[1]])
            debris_list["BR"].append([brick_rect.bottomright[0], brick_rect.bottomright[1]])
            debris_list["TL"].append([brick_rect.topleft[0], brick_rect.topleft[1]])
            debris_list["TR"].append([brick_rect.topright[0], brick_rect.topright[1]])
            hit_box_list.remove(brick_rect)

def draw_debris():
    for i, x in enumerate(debris_list["BL"]):
        x[0] -= debris_vx 
        if x[1] < debris_list["DEBRIS"][i].bottomleft[1] - 30:
            debris_list["Y"][i] = 4
        x[1] += debris_list["Y"][i]
        draw_on_bg(brick_debris_bottom_left, x)
    for i, x in enumerate(debris_list["BR"]):
        x[0] += debris_vx 
        x[1] += debris_list["Y"][i]
        draw_on_bg(brick_debris_bottom_right, x)
    for i, x in enumerate(debris_list["TL"]):
        x[0] -= debris_vx 
        x[1] += debris_list["Y"][i]
        draw_on_bg(brick_debris_top_left, x)
    for i, x in enumerate(debris_list["TR"]):
        x[0] += debris_vx 
        x[1] += debris_list["Y"][i]
        draw_on_bg(brick_debris_top_right, x)
    if debris_list["BL"][0][1] >= 456 and debris_list["BR"][0][1] >=456 \
    and debris_list["TL"][0][1] >= 456 and debris_list["TR"][0][1] >= 456: #continue the next line
        debris_list["DEBRIS"].pop(0)
        debris_list["Y"].pop(0)
        debris_list["BL"].pop(0)
        debris_list["BR"].pop(0)
        debris_list["TL"].pop(0)
        debris_list["TR"].pop(0)
        

def draw_empty_brick_rect(question_rect): 
    if question_rect in empty_brick_list:
        draw_on_bg(empty_brick, rect = question_rect)

def draw_coin_rect(question_rect, coin_rect):
    if colliderect_on_bg_bottom(mario_rect, question_rect):
        coin_list .append(coin_rect)
        empty_brick_list.append(question_rect)
        
    if coin_rect in coin_list :
        draw_on_bg(coin, rect = coin_rect)
        coin_jump(coin_rect, question_rect)

    draw_empty_brick_rect(question_rect) 

def coin_jump(coin_rect, question_rect):
    global m
    global v

    if coin_rect.y == question_rect.y:
        coin_sound.play()
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
    for coin in coin_list :
        if coin == coin_rect:
            coin_list .remove(coin_rect)
    
def draw_mushroom_or_flower_rect(question_rect, red_mushroom_rect, flower_rect):
    if colliderect_on_bg_bottom(mario_rect, question_rect):
        empty_brick_list.append(question_rect)
        if mario_size == 0:
            mushroom_list.append(red_mushroom_rect)
            drawn_mushroom_list.append(red_mushroom_rect) #make sure only either mushroom or flower pop up once
        elif mario_size == 1 and red_mushroom_rect not in drawn_mushroom_list and flower_rect not in drawn_flower_list:
            flower_list.append(flower_rect)
            drawn_flower_list.append(flower_rect) #make sure only either mushroom or flower pop up once

    if red_mushroom_rect in mushroom_list:
        draw_on_bg(red_mushroom, rect = red_mushroom_rect)
        mushroom_flower_rise(red_mushroom_rect, question_rect)

    if flower_rect in flower_list:
        global flower_count
        flower_count += 0.1
        if flower_count >= 3:
            flower_count = 0
        draw_on_bg(flower[int(flower_count)], rect = flower_rect)
        mushroom_flower_rise(flower_rect, question_rect)

    remove_mushroom_or_flower_rect(red_mushroom_rect, flower_rect)
    draw_empty_brick_rect(question_rect)

def mushroom_flower_rise(mushroom_flower_rect, question_rect):
    if (question_rect.top - mushroom_flower_rect.top) == 2:
        powerup_pop_sound.play()
    if ((mushroom_flower_rect.midbottom[1] >= question_rect.midtop[1]) and 
       not(mushroom_flower_rect.bottom <= question_rect.top)):
        mushroom_flower_rect.y -= 1

def remove_mushroom_or_flower_rect(red_mushroom_rect, flower_rect):
    global mario_size
    global start_time_grow
    if colliderect_on_bg(mario_rect, red_mushroom_rect):
        for mushroom in mushroom_list:
            if mushroom == red_mushroom_rect:
                mushroom_list.remove(red_mushroom_rect)
                powerup_eat_sound.play()
                start_time_grow = pygame.time.get_ticks()
                mario_size = 1
    if colliderect_on_bg(mario_rect, flower_rect):
        for flower in flower_list:
            if flower == flower_rect:
                flower_list.remove(flower_rect)
                powerup_eat_sound.play()

def mario_grow():
    global mario_size
    global mario_rect
    mario_size = 1
    # Make the mario_rect fits the new bigmario
    mario_rect = bigmario_list[4].get_rect(bottomleft = (mario_rect.left, mario_rect.bottom))

def mario_shrink():
    global mario_size
    global mario_rect
    mario_size = 0
    mario_rect = mario.get_rect(bottomleft = (mario_rect.left, mario_rect.bottom))

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

def update_lives():
    # call this funcion everytime mario dies 
    # UNFINISHED
    global lives_value
    lives_value -= 1 
    if lives_value == 0:
        pass
        # black screen it 

# example code on adding score once
# mario touches the pole, To be ameliorated


def endgameSequence():
    global moving_right
    global flag_y_pos
    global jump_logic
    global endgame_delay
    global flag_mario_drop

    current_playing_music = check_music_playing()
    if current_playing_music:
        current_playing_music.stop()
    pygame.event.set_blocked([pygame.KEYDOWN, pygame.KEYUP])
    moving_right = False    #Disable movement so mario sticks on the pole
    jump_logic = False      #Stop mario from sliding down the pole
    endgame_delay += 1
    if endgame_delay == 30: #Wait a brief before dropping flag and mario drop
        flag_mario_drop = True
        flag_song.play()
    
    if flag_mario_drop == True:   #Drops the flag to the floor
        if flag_y_pos<336:
            flag_y_pos += 4
        if mario_rect.y <336:
            mario_rect.y += 4

          
def check_pole():
    global score_value
    global bonus_score

    if colliderect_on_bg(mario_rect, pole_rect):
        
        endgameSequence()

        bonus_score += 1
        if bonus_score == 1:

            if mario_rect.y <= 93:
                score_value += 5000
            elif mario_rect.y <=  148:
                score_value += 4000
            elif mario_rect.y <=  203:
                score_value += 3000
            elif mario_rect.y <=  258:
                score_value += 2000
            elif mario_rect.y <=  313:
                score_value += 1000
            elif mario_rect.y <= 368:
                score_value += 100 
        
def check_music_playing():
    if main_theme_song.get_num_channels() >= 1:
        return main_theme_song
    if main_theme_speedup.get_num_channels() >= 1:
        return main_theme_speedup
    return None 
#bg_music_check
def mario_bg_music():
    global main_theme_play
    global main_theme_fastvers
    seconds=(pygame.time.get_ticks()-time_ticks)/600
    if mario_dead == False:
        if mario_state == 0:
            if (time_value - int(seconds)) > 100:
                if main_theme_play == False:
                    main_theme_play = True
                    main_theme_song.play()
            else:
                main_theme_play = False
                main_theme_song.stop()
                if main_theme_fastvers == False:
                    main_theme_fastvers = True
                    main_theme_speedup.play()
        elif mario_state == 1:
            main_theme_play = False
            main_theme_fastvers = False
            main_theme_song.stop()
            main_theme_speedup.stop()
    if mario_dead == True:
        if main_theme_play == True:
            main_theme_play = False
            main_theme_song.stop()
        if main_theme_fastvers == True:
            main_theme_fastvers = False
            main_theme_speedup.stop()

def limit_speed(dir = 0):
    global acceleration_x
    global acceleration_vx 
    global velocity_x
    
    if dir == 0: #left
        if acceleration_x <= -maximum_acceleration_x:
            acceleration_x = -maximum_acceleration_x
        else:
            acceleration_x-= acceleration_vx 
        if velocity_x >= maximum_velocity:
            velocity_x = maximum_velocity
        else:
            velocity_x -= acceleration_x * delta_time
    elif dir == 1: #right
        if acceleration_x >= maximum_acceleration_x:
            acceleration_x = maximum_acceleration_x
        else:
            acceleration_x += acceleration_vx 
        if velocity_x >= maximum_velocity:
            velocity_x = maximum_velocity
        else:
            velocity_x += acceleration_x * delta_time

def skiing_effect_left():
    global velocity_x
    global skied_left 
    global mario_rect
    global acceleration_x 

    if acceleration_x < 0:
        if velocity_x > 0: 
            velocity_x += (acceleration_x * delta_time)/4
            # positive += negative = negative
        else:
            velocity_x = 0
        acceleration_x += ski_acceleration
        if mario_rect.x >= 0:
            mario_rect.x -= abs(velocity_x + 0.5*acceleration_x*(delta_time*delta_time)) 

    else:
        acceleration_x = 0
        velocity_x = 0
        skied_left = True
    
def skiing_effect_right():
    global velocity_x
    global bg_x_pos
    global skied_right
    global mario_rect
    global acceleration_x 

    if acceleration_x > 0:
        if velocity_x > 0: 
            velocity_x -= (acceleration_x * delta_time)/4
            #positive -= positive = negative
        else:
            velocity_x = 0
        acceleration_x -= ski_acceleration
        if mario_rect.x < (575 - marioW):     #limit mario's movement to before the mid sectiond
            # d = vt + 1/2 at^2
            how_far_it_goes = abs(velocity_x + 0.5*acceleration_x*(delta_time*delta_time)) 
            if how_far_it_goes < 1: 
                how_far_it_goes = 1
            mario_rect.x += how_far_it_goes
        else:
            bg_x_pos -= abs(velocity_x + 0.5*acceleration_x *(delta_time*delta_time)) 

    else:
        acceleration_x = 0
        velocity_x = 0
        skied_right = True
        
while True:
    check_pole() # TBD
    # The floors for mario to stand on
    draw_floor() #draw the floor before the BG 
    screen.blit(bg, (bg_x_pos,0)) #draw BG 
    draw_on_bg(pole, rect = pole_rect)
    draw_on_bg(pole_ball, pole_ball_co)

    flag_animation_i += 0.1
    if flag_animation_i >= 10:
        flag_animation_i = 0
    flag_co = (6283, (flag_y_pos))
    draw_on_bg(flag_animation_list[int(flag_animation_i)], flag_co)
    mario_bg_music()

    # ~ Mario dead logic 
    if mario_dead == False:
        # timer to decrease the 400 times 
        # in Mario, 1 sec is 0.6 sec in real life 
        seconds=(pygame.time.get_ticks()-time_ticks)/600
        if (time_value - int(seconds)) <= 0:
            mario_dead = True
    else:
        # these are the things that only have to 
        # happen ONE TIME after mario died
        if mario_died_one_time == False:
            # pause all other musics
            mario_died_x = mario_rect.x
            mario_died_y = mario_rect.y
            mario_died_one_time = True
            mario_dead_sound.play()
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
    for i, goomba_i in enumerate(enemy_list):
        # need to change goomba_alive to goomba_i.alive
        if (enemy_list_alive[i] == True) and (abs(goomba_i.x - abs(bg_x_pos)) <= 1000):
            goomba_i.x -= 1

        # goomba animation
        goomba_animation_i += 0.005
        if goomba_animation_i >= 2:
            goomba_animation_i = 0


        # check collsion
        if (colliderect_on_bg(mario_rect, goomba_i) and (on_ground == False)) == True:
            if enemy_list_alive[i] == True:
                jump = True
                stomp_sound.play()
                max_height = goomba_i.bottom - 50
                enemy_list_alive[i] = False
        elif (colliderect_on_bg(mario_rect, goomba_i) and enemy_list_alive[i]) == True:
            if enemy_list_alive[i] == True:
                if mario_size == 1:
                    mario_shrink()
                    mario_state = -1 # temp invincible
                    temp_invincible = pygame.time.get_ticks()
                    pipe_sound.play() # somehow it's pipe sound lol
                elif mario_state == 0:
                    mario_dead = True
                elif mario_state == 1:
                    enemy_list_alive[i] = False 

        mario_after_invincible_time = pygame.time.get_ticks()
        
        # ~ Temporary invincible after big mario shrinked
        if temp_invincible: 
            mario_temp_inv_effect += 1 
            print(mario_state)
            print(mario_size)
            if mario_temp_inv_effect == 50:
                mario_size = 99999 # doesn't exist, so the game won't blit
                                   # thus creating the invincible effect
                mario_temp_inv_effect = 0
            elif mario_temp_inv_effect == 25: 
                mario_size = 0
            if mario_after_invincible_time - temp_invincible >= 2000:
                temp_invincible = 0
                mario_state = 0
                mario_size = 0
                mario_temp_inv_effect = 0

        # goomba render
        if enemy_list_alive[i] == True:
            draw_on_bg(goomba_animation_list[int(goomba_animation_i)], rect = goomba_i)
        elif enemy_list_alive[i] == False:
            draw_on_bg(goomba_death_ani, (goomba_i.x, (goomba_i.y + int(goomba_i.height / 2))))
            # LET Goomba's corpse stay there for 1 sec
            if goomba_ticks[i] == 0:
                goomba_ticks[i] = pygame.time.get_ticks()
            goomba_count_tick = pygame.time.get_ticks()
            if goomba_count_tick - goomba_ticks[i] >= 1000:
                goomba_ticks.pop(i)
                enemy_list.remove(goomba_i)
                enemy_list_alive.pop(i)

        if (abs(goomba_i.x - abs(bg_x_pos)) <= 0):
            # remove them so as to increase the game's performance 
            # no need to process unnecessary information
            enemy_list.remove(goomba_i)
            enemy_list_alive.pop(i)
            
    if mario_rect.y >= 448:
        mario_dead = True
    #### #### #### #### #### BEN's end #### #### #### #### #### ####

    #### #### #### #### #### YUN SION's #### #### #### #### #### ####
    draw_on_bg(titleBanner, (37.5, 75)) 
    draw_on_bg(copywrite, (200, 250))

    # Gameover scene # 
    # when mario dies, play this #
    # screen.fill((0,0,0))
    # screen.blit(gameoverText,gameoverText_rect)
    # game_over_sound.play(loops=0,maxtime=0,fade_ms=0)
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
    if colliderect_on_bg_bottom(mario_rect, coin_brick_rect):
        count_coin += 1

        # Only draw coin for the first time of collision
        if count_coin == 1:            
            coin_sound.play()
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
    if colliderect_on_bg_bottom(mario_rect, star_brick_rect):
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
        mario_state = 1
        start_time_invincible = pygame.time.get_ticks()
        if invincible__music == False:
            invincible__music = True
            invincible_music.play()

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

    draw_mushroom_or_flower_rect(question_rect10, red_mushroom_rect1, flower_rect1)
    draw_mushroom_or_flower_rect(question_rect11, red_mushroom_rect2, flower_rect2)
    draw_mushroom_or_flower_rect(question_rect12, red_mushroom_rect3, flower_rect3)
    # Small invincible flash
    invincible_count += 0.1
    if invincible_count >= 3:
        invincible_count = 0

    # ~ Display invincible only for 10 seconds
    if start_time_invincible:
        time_taken = pygame.time.get_ticks() - start_time_invincible
        if time_taken >= 10000:
            if invincible__music == True:
                invincible__music = False
                invincible_music.stop() 
            mario_state = 0
            start_time_invincible = 0

    # Disable the user to move mario until mario becomes big and sound effect ends
    if start_time_grow:
        transform_time_taken += 1
        if mario_size == 0 and transform_time_taken >= transform_interval:
            transform_time_taken = 0
            mario_grow()
        elif mario_size > 0 and transform_time_taken >= transform_interval:
            transform_time_taken = 0
            mario_shrink()

        acceleration_x = 0
        velocity_x = 0
        moving_left = False
        moving_right = False
        mario_count = 4
        pygame.event.set_blocked([pygame.KEYDOWN, pygame.KEYUP])

        time_taken = pygame.time.get_ticks() - start_time_grow
        if time_taken >= powerup_eat_length * 1000:
            mario_grow()
            start_time_grow = 0
            pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])
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
                    # in case player press left and then press right 
                    # without letting go the left key 
                    if moving_left == True:
                        skied_left = False
                        moving_left = False  
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT: 
                    moving_left = True
                    # in case player press right and then press left 
                    # without letting go the right key 
                    if moving_right == True:
                        skied_right = False
                        moving_right = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if on_ground == True: #makes it run only once 
                        max_height = default_on_ground_y - JUMP_HEIGHT
                        on_ground = False
                        jump = True
                if event.key == pygame.K_LSHIFT:
                    maximum_velocity = 5 #increase velocity

        # ~ DISABLE MOVE/JUMP 
            if event.type == pygame.KEYUP:  
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if moving_right == True:
                        skied_right = False
                        moving_right = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if moving_left == True:
                        skied_left = False
                        moving_left = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    jump = False
                if event.key == pygame.K_LSHIFT:
                    maximum_velocity = 3 #increase velocity

    if mario_dead == True:
        # disable control after dead
        moving_right = False
        moving_left = False
        mario_count = 4
        jump = False

    # ~ JUMP's logic 
    if jump_logic == True:#NAZ
        if jump == True:
            mario_count = 5
            # ~ Give mario gravity 
            mario_m = 0.5
            if mario_rect.bottom == default_on_ground_y:
                small_jump_sound.play()
            if mario_rect.bottom > max_height:
                F = 0.5 * mario_m * (velocity_y ** 2)
                if velocity_y > 0:
                    velocity_y -= 0.13
                else:
                    velocity_y = 0
            mario_rect.y -= F #goes up 
            # # # # # # # # # # # # # 
            if mario_rect.bottom <= max_height:
                mario_rect.bottom = max_height
                velocity_y = 1.3
                jump = False
        else:
            mario_m = -0.5
            F = 0.5 * mario_m * (velocity_y ** 2)
            if velocity_y < 6:
                velocity_y += 0.13
                if velocity_y == 6:
                    velocity_y = 6.1
                # increase velocity to 6 
            elif velocity_y == 6:
                velocity_y = 3

            mario_rect.y -= F #goes down
            if on_ground:
                if moving_left or moving_right == True:
                    mario_count += 0.1
                    if mario_count >= 4:
                        mario_count = 0 
                else:
                    mario_count = 4
    
    check_collisonsy() # check vertical collision immediately so mario don't jump thru blocks, or go thru floors.

    # WALK's logics
    
    # Happened when mario done walking 
    # or change direction immediately

    # ~ Skiing effects! 
    if mario_dead == False:
        # dont ski if died lol
        if skied_right == False:
            skiing_effect_right() 
        if skied_left == False:
            skiing_effect_left() 

    if moving_right == True:
        direction = facing_right 
        if bg_x_pos > bgLimit:                   #logic to stop when limit is reached
            limit_speed(1)  
                
            if mario_rect.x < (575 - marioW):     #limit mario's movement to before the mid sectiond
                # d = vt + 1/2 at^2
                mario_rect.x += velocity_x + (0.5 * acceleration_x * (delta_time**2))
            else:
                bg_x_pos -= velocity_x + (0.5 * acceleration_x * (delta_time**2))          #after reaching the middle, background will move
        else: #mario reaches the end
            limit_speed(1)  
            mario_rect.x += velocity_x + (0.5 * acceleration_x * (delta_time**2)) 

    elif moving_left == True:
        direction = facing_left 
        if mario_rect.x >= 0:
            limit_speed(0)  
            mario_rect.x -= velocity_x + (0.5 * acceleration_x * (delta_time**2))
    check_collisonsx() # check horizontal collision immediately so mario don't walk past rects like Pipes

    # ~ JUMP and WALK animation 
    # ~ Play invincible if mario_state = 1
    if mario_dead == False:
        if on_ground == False:
            mario_count = 5
        if direction == -1:
            if (mario_size == 0 and mario_state == 0) or (mario_size == 0 and mario_state == -1):
                screen.blit(marioflip[int(mario_count)], (mario_rect.x,mario_rect.y))
            elif mario_size == 1 and mario_state == 0:
                screen.blit(bigmario_flip[int(mario_count)], (mario_rect.x, mario_rect.y))
            elif mario_size == 1 and mario_state == 2:
                screen.blit(firemario_flip[int(mario_count)], (mario_rect.x, mario_rect.y))
            elif mario_size == 0 and mario_state == 1:
                screen.blit(small_invincible_flip[int(invincible_count)][int(mario_count)], (mario_rect.x,mario_rect.y))
            elif mario_size == 1 and mario_state == 1:
                screen.blit(big_invincible_flip[int(invincible_count)][int(mario_count)], (mario_rect.x,mario_rect.y))
        else:
            if (mario_size == 0 and mario_state == 0) or (mario_size == 0 and mario_state == -1):
                screen.blit(animation_list[int(mario_count)], (mario_rect.x,mario_rect.y))
            elif mario_size == 1 and mario_state == 0:
                screen.blit(bigmario_list[int(mario_count)], (mario_rect.x, mario_rect.y))
            elif mario_size == 1 and mario_state == 2:
                screen.blit(firemario_list[int(mario_count)], (mario_rect.x, mario_rect.y))
            elif mario_size == 0 and mario_state == 1:
                screen.blit(small_invincible_list[int(invincible_count)][int(mario_count)], (mario_rect.x,mario_rect.y))
            elif mario_size == 1 and mario_state == 1:
                screen.blit(big_invincible_list[int(invincible_count)][int(mario_count)], (mario_rect.x,mario_rect.y))
    else:
        screen.blit(mario_died_pic,(mario_died_x, mario_died_y))
    #### #### #### #### #### RAJA's end #### #### #### #### #### ####

    if debris_list["DEBRIS"]:
        draw_debris()
    pygame.display.update()  #update screen
    # Friction
    delta_time = clock.tick(TARGET_FPS) * 0.001 * TARGET_FPS  #clock.tick(FPS) limit our game to 60 fps no matter what
