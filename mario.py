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

# star rect didn't dissapear, become inv again if touch it
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

####### GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET #####  
def reset_game():
    # one of the reasons why you want to use class
    # too many global when it comes to things like this
    global bg_x_pos
    global mario_rect
    global mario_size
    global mario_state
    global mario_dead
    global mario_died_one_time
    global draw_coin
    global draw_star
    global start_time_invincible
    global goomba1_alive
    global goomba2_alive
    global goomba3_alive
    global goomba4_alive
    global goomba5_alive
    global goomba6_alive
    global goomba7_alive
    global goomba8_alive
    global goomba9_alive
    global goomba10_alive
    global goomba11_alive
    global goomba12_alive
    global goomba13_alive
    global goomba14_alive
    global goomba15_alive
    global goomba16_alive
    global goomba1
    global goomba2
    global goomba3
    global goomba4
    global goomba5
    global goomba6
    global goomba7
    global goomba8
    global goomba9
    global goomba10
    global goomba11
    global goomba12
    global goomba13
    global goomba14
    global goomba15
    global goomba16
    global coin_rect0
    global coin_rect1
    global coin_rect2
    global coin_rect3
    global coin_rect4
    global coin_rect5
    global coin_rect6
    global coin_rect7
    global coin_rect8
    global coin_rect9
    global enemy_list
    global enemy_list_alive
    global goomba_ticks
    global on_ground
    global score_value
    global coins_value
    global time_ticks
    global main_theme_play
    global main_theme_fastvers
    global invincible_music_played
    global after_life_time
    global coin_list
    global mushroom_list
    global flower_list
    global remove_brick_list
    global drawn_mushroom_list
    global drawn_flower_list
    global empty_brick_list
    global seconds
    global mario_dead_velo
    global debris_list
    global hit_box_list
    global red_mushroom_rect1
    global red_mushroom_rect2
    global red_mushroom_rect3
    global star_rect
    global flower_rect1
    global flower_rect2
    global flower_rect3
    global count_star
    global red_mushroom_rect1
    global red_mushroom_rect2
    global red_mushroom_rect3
    global mushroom_hit_box_list_x
    global mushroom_hit_box_list_y
    global mushroom_vel_x
    global collided
    global mushroom_dropping
    global mushroom_finish_rising
    global mushroom_count
    global troller
    global start_time_coin
    global count_coin
    global draw_empty_brick

    bg_x_pos = 0
    mario_rect = mario.get_rect(bottomleft = (40, 400))
    mario_size = 0
    mario_state = 0
    start_time_invincible = 0
    mario_dead = False
    mario_died_one_time = False
    draw_coin = False
    draw_star = False
    goomba_animation_list[0] = pygame.transform.scale(goomba_animation_list[0], (32, 32))
    goomba_animation_list[1] = pygame.transform.scale(goomba_animation_list[1], (32, 32))
    goomba1 = goomba_animation_list[0].get_rect(topleft = (680, 368))
    goomba2 = goomba_animation_list[0].get_rect(topleft = (1300, 368))
    goomba3 = goomba_animation_list[0].get_rect(topleft = (1620, 368))
    goomba4 = goomba_animation_list[0].get_rect(topleft = (1680, 368))
    goomba5 = goomba_animation_list[0].get_rect(topleft = (2572, 368))
    goomba6 = goomba_animation_list[0].get_rect(topleft = (2630, 368))
    goomba7 = goomba_animation_list[0].get_rect(topleft = (3110, 368))
    # turtle = (1705, 368)
    goomba8 = goomba_animation_list[0].get_rect(topleft = (3170, 368))
    goomba9 = goomba_animation_list[0].get_rect(topleft = (3650, 368))
    goomba10 = goomba_animation_list[0].get_rect(topleft = (3710, 368))
    goomba11 = goomba_animation_list[0].get_rect(topleft = (3960, 368))
    goomba12 = goomba_animation_list[0].get_rect(topleft = (4020, 368))
    goomba13 = goomba_animation_list[0].get_rect(topleft = (4100, 368))
    goomba14 = goomba_animation_list[0].get_rect(topleft = (4160, 368))
    goomba15 = goomba_animation_list[0].get_rect(topleft = (5570, 368))
    goomba16 = goomba_animation_list[0].get_rect(topleft = (5630, 368))
    enemy_list = [goomba1, goomba2, goomba3, goomba4, goomba5, goomba6, goomba7, goomba8, goomba9, goomba10, goomba11, goomba12, goomba13, goomba14, goomba15, goomba16]
    coin_rect0 = coin.get_rect(midtop = (3023, 272))
    coin_rect1 = coin.get_rect(midtop = (527, 272))
    coin_rect2 = coin.get_rect(midtop = (752, 272))
    coin_rect3 = coin.get_rect(midtop = (719, 144))
    coin_rect4 = coin.get_rect(midtop = (3023, 144))
    coin_rect5 = coin.get_rect(midtop = (3407, 272))
    coin_rect6 = coin.get_rect(midtop = (3502, 272))
    coin_rect7 = coin.get_rect(midtop = (3598, 272))
    coin_rect8 = coin.get_rect(midtop = (4143, 144))
    coin_rect9 = coin.get_rect(midtop = (5455, 272))
    goomba1_alive = True
    goomba2_alive = True
    goomba3_alive = True
    goomba4_alive = True
    goomba5_alive = True
    goomba6_alive = True
    goomba7_alive = True
    goomba8_alive = True
    goomba9_alive = True
    goomba10_alive = True
    goomba11_alive = True
    goomba12_alive = True
    goomba13_alive = True
    goomba14_alive = True
    goomba15_alive = True
    goomba16_alive = True
    enemy_list_alive = [goomba1_alive, goomba2_alive, goomba3_alive, goomba4_alive, goomba5_alive, goomba6_alive, goomba7_alive, goomba8_alive, goomba9_alive, goomba10_alive, goomba11_alive, goomba12_alive, goomba13_alive, goomba14_alive, goomba15_alive, goomba16_alive]
    goomba_ticks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    on_ground = True
    score_value = 0
    coins_value = 0
    time_ticks = pygame.time.get_ticks() 
    seconds = 0
    main_theme_play = False
    main_theme_fastvers = False
    invincible_music_played = False
    after_life_time = 0
    coin_list  = []
    mushroom_list = []
    flower_list = []
    remove_brick_list = []
    drawn_mushroom_list = []
    drawn_flower_list = []
    empty_brick_list = []
    mario_dead_velo = -3
    debris_list = {"DEBRIS": [], "Y": [],
                "BL": [], "BR": [], 
                "TL": [], "TR": []}
    hit_box_list = [question_rect1,question_rect2,question_rect3,question_rect4,question_rect5,question_rect6,
                question_rect7,question_rect8,question_rect9,question_rect10,question_rect11,question_rect12,
                pipe1_rect, pipe2_rect, pipe3_rect, pipe4_rect, pipe5_rect, pipe6_rect, floor1, floor2, floor3, floor4,
                brick_rect1, brick_rect2, brick_rect3, brick_rect4, brick_rect5, brick_rect6, brick_rect7,
                brick_rect8, brick_rect9, brick_rect10, brick_rect11, brick_rect12, brick_rect13, brick_rect14,
                brick_rect15, brick_rect16, brick_rect17, brick_rect18, brick_rect19, brick_rect20, brick_rect21,
                brick_rect22, brick_rect23, brick_rect24, brick_rect25, brick_rect26, brick_rect27, brick_rect28,
                brick_rect29, coin_brick_rect, star_brick_rect, rock_rect1, rock_rect2, rock_rect3, rock_rect4,
                rock_rect5, rock_rect6, rock_rect7, rock_rect8, rock_rect9, rock_rect10, rock_rect11, rock_rect12,
                rock_rect13, rock_rect14, rock_rect15, rock_rect16, rock_rect17, rock_rect18, rock_rect19, rock_rect20,
                rock_rect21, rock_rect22, rock_rect23, rock_rect24, rock_rect25, rock_rect26, rock_rect27, rock_rect4_1,
                rock_rect4_2, rock_rect4_3, rock_rect5_1, rock_rect5_2, rock_rect5_3, rock_rect13_1, rock_rect13_2, rock_rect13_3,
                rock_rect14_1, rock_rect14_2, rock_rect14_3, rock_rect26_1, rock_rect26_2, rock_rect26_3, rock_rect26_4,
                rock_rect26_5, rock_rect26_6, rock_rect26_7]
    red_mushroom_rect1 = red_mushroom_list[0].get_rect(topleft = (672, 270))
    red_mushroom_rect2 = red_mushroom_list[0].get_rect(topleft = (2494, 270))
    red_mushroom_rect3 = red_mushroom_list[0].get_rect(topleft = (3486, 142))
    mushroom_count = 0
    mushroom_finish_rising = False
    mushroom_dropping = False
    collided = False
    mushroom_vel_x = 1.5
    mushroom_hit_box_list_x = [rock_rect1, pipe1_rect]
    mushroom_hit_box_list_y = [question_rect2, question_rect7, question_rect10, question_rect11, question_rect12, 
                                brick_rect2, brick_rect3, brick_rect5, floor1, floor2, floor3, floor4]
    star_rect = star[0].get_rect(topleft = (3231, 270))
    flower_rect1 = flower[0].get_rect(topleft = (672, 270))
    flower_rect2 = flower[0].get_rect(topleft = (2494, 270))
    flower_rect3 = flower[0].get_rect(topleft = (3486, 142))
    count_star = 0
    troller = False
    start_time_coin = 0
    count_coin = 0
    draw_empty_brick = False

####### GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET GAME RESET #####   
def restart_game(time_interval = 5000):
    """
    float: time_interval, milliseconds
    """
    global lives_value 
    after_dead_time = pygame.time.get_ticks()
    if after_life_time:
        if after_dead_time - after_life_time > time_interval:
            lives_value -= 1
            if lives_value > -1:
                reset_game()

def game_over_screen():
    global after_life_time
    global game_over_song_played
    global game_over_song_timer
    after_life_time = 0
    screen.fill(BLACK)
    screen.blit(game_over_font, (500 - game_over_font.get_width()/2, 224 - game_over_font.get_height()/2))
    if game_over_song_played == False:
        game_over_song_timer = pygame.time.get_ticks()
        game_over_song.play()
        game_over_song_played = True
    game_over_song_time = pygame.time.get_ticks()
    if game_over_song_time - game_over_song_timer > game_over_song_length:
        sys.exit()
    # play gameover music
    # display gameover text

def display_top_texts():
    
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
def check_collisonsx(temp_fireball_rect = None):
    global mario_rect
    global hit_box_list
    global mario_count
    global acceleration_x
    global velocity_x
    global skied_left
    global skied_right
    global fireBall_rect_list
    """
    enemy: False is victim is not enemy, True if victim is enemy
    - Therefore we can let mario dies if he hits an enemy instead of wall
    """
    for hit_box in hit_box_list:
        # 896 -> 896 -> 896 
        # 0 -> 100 -> 200 -> 500 

        temp_hit_box = copy(hit_box)
        temp_hit_box.x += bg_x_pos
        if temp_fireball_rect == None:
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
        elif temp_fireball_rect:
            if temp_fireball_rect.colliderect(temp_hit_box):
                return temp_hit_box
        
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
            update_score(50)
        remove_brick_list.append(brick_rect) #Reverse, works
        remove_brick_rect(brick_rect) #remove the rect 
    elif mario_size == 0 and colliderect_on_bg_bottom(mario_rect, brick_rect):
        if brick_rect not in remove_brick_list: #don't draw if it's collided
            bump_sound.play()
            bumping_brick = brick_rect
            bumping_brick_ori_y = brick_rect.y
        #move the brick up a bit
    if bumping_brick:
        # fix double bugs
        bumping_brick.y += bumping_brick_velo_y 
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
        coin_list.append(coin_rect)
        empty_brick_list.append(question_rect)
        
    if coin_rect in coin_list:
        draw_on_bg(coin, rect = coin_rect)
        coin_jump(coin_rect, question_rect)

    draw_empty_brick_rect(question_rect) 

def coin_jump(coin_rect, question_rect):
    global m
    global v

    if coin_rect.y == question_rect.y:
        coin_sound.play()
        update_coins()
        update_score(200)
    if not coin_rect.y > question_rect.y:
        F = (1/2) * m * (v ** 2)
        coin_rect.y -= F
        v -= 0.25
        if v < 0:
            m = -1
    else:
        remove_coin_rect(coin_rect)
        m = 1
        v = 5

def remove_coin_rect(coin_rect):
    for coin in coin_list:
        if coin == coin_rect:
            coin_list.remove(coin_rect)
    
def draw_mushroom_or_flower_rect(question_rect, red_mushroom_rect, flower_rect):
    global mushroom_finish_rising
    global mushroom_vel_x
    if colliderect_on_bg_bottom(mario_rect, question_rect):
        empty_brick_list.append(question_rect)
        if mario_size == 0 or mario_size == 99999:
            mushroom_list.append(red_mushroom_rect)
            drawn_mushroom_list.append(red_mushroom_rect) #make sure only either mushroom or flower pop up once
            mushroom_finish_rising = False
            mushroom_vel_x = 1.5
        elif (mario_size == 1 or mario_size == 2) and red_mushroom_rect not in drawn_mushroom_list and flower_rect not in drawn_flower_list:
            flower_list.append(flower_rect)
            drawn_flower_list.append(flower_rect) #make sure only either mushroom or flower pop up once

    if red_mushroom_rect in mushroom_list:
        draw_on_bg(red_mushroom, rect = red_mushroom_rect)
        mushroom_rise(red_mushroom_rect, question_rect)

    if flower_rect in flower_list:
        global flower_count
        flower_count += 0.1
        if flower_count >= 3:
            flower_count = 0
        draw_on_bg(flower[int(flower_count)], rect = flower_rect)
        flower_rise(flower_rect, question_rect)

    remove_mushroom_or_flower_rect(red_mushroom_rect, flower_rect)
    draw_empty_brick_rect(question_rect)

def mushroom_rise(mushroom_rect, question_rect):
    global mushroom_finish_rising
    global mushroom_vel_x
    global mushroom_vel_y
    global mushroom_dropping

    if (question_rect.top - mushroom_rect.top) == 2 and mushroom_finish_rising == False:
        powerup_pop_sound.play()

    if (mushroom_rect.bottom >= question_rect.top) and mushroom_finish_rising == False:
        mushroom_rect.y -= 1
    else:
        mushroom_finish_rising = True
        
    if mushroom_finish_rising:
        troll_goomba(mushroom_rect)
        mushroom_rect.x += mushroom_vel_x
        if mushroom_dropping:
            mushroom_rect.y += mushroom_vel_y
        check_mushroom_x(mushroom_rect)
        check_mushroom_y(mushroom_rect)

def flower_rise(flower_rect, question_rect):
    if (question_rect.top - flower_rect.top) == 2:
        powerup_pop_sound.play()
    if ((flower_rect.midbottom[1] >= question_rect.midtop[1]) and 
       not(flower_rect.bottom <= question_rect.top)):
        flower_rect.y -= 1
        
def remove_mushroom_or_flower_rect(red_mushroom_rect, flower_rect):
    global start_time_grow
    if colliderect_on_bg(mario_rect, red_mushroom_rect):
        for mushroom in mushroom_list:
            if mushroom == red_mushroom_rect:
                mushroom_list.remove(red_mushroom_rect)
                powerup_eat_sound.play()
                update_score(1000)
                start_time_grow = pygame.time.get_ticks()

    if colliderect_on_bg(mario_rect, flower_rect):
        for flower in flower_list:
            if flower == flower_rect:
                flower_list.remove(flower_rect)
                powerup_eat_sound.play()
                update_score(1000)
                mario_grow_fire()

def check_mushroom_x(mushroom_rect):
    global mushroom_hit_box_list_x
    global mushroom_count
    global mushroom_vel_x
    global mushroom_dropping
    
    for hit_box in mushroom_hit_box_list_x:
        if mushroom_rect.colliderect(hit_box):
            if mushroom_vel_x > 0:
                mushroom_vel_x = -1.5
                mushroom_count = 1
            elif mushroom_vel_x < 0:
                mushroom_vel_x = 1.5
                mushroom_count = 0

def check_mushroom_y(mushroom_rect):
    global mushroom_hit_box_list_y
    global mushroom_vel_y
    global mushroom_dropping
    global collided

    for hit_box in mushroom_hit_box_list_y:
        if mushroom_rect.colliderect(hit_box):
            collided = True

    if collided:
        mushroom_dropping = False
        collided = False
    else:
        mushroom_dropping = True
        
def mario_grow():
    global mario_size
    global mario_rect
    mario_size = 1
    # Make the mario_rect fits the new bigmario
    mario_rect = bigmario_list[4].get_rect(bottomleft = (mario_rect.left, mario_rect.bottom))

def mario_grow_fire():
    global mario_size
    global mario_rect
    global temp_invincible
    global mario_temp_inv_effect
    global mario_state
    mario_size = 2
    # Make the mario_rect fits the new bigmario
    mario_rect = bigmario_list[4].get_rect(bottomleft = (mario_rect.left, mario_rect.bottom))
    # in case eaten fire when temporary invincible 
    temp_invincible = 0
    if mario_state != 1:
        mario_state = 0
    mario_temp_inv_effect = 0

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
    # return the music it is now playing, return None if no
    if main_theme_song.get_num_channels() >= 1:
        return main_theme_song
    if main_theme_speedup.get_num_channels() >= 1:
        return main_theme_speedup
    return None 
    
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

def blit_mario():
    global mario_dead
    global on_ground
    global direction
    global mario_size
    global mario_state
    global mario_count
    
    if mario_dead == False:
        if on_ground == False:
            mario_count = 5
        if direction == -1:
            if (mario_size == 0 and mario_state == 0) or (mario_size == 0 and mario_state == -1):
                screen.blit(marioflip[int(mario_count)], (mario_rect.x,mario_rect.y))
            elif mario_size == 1 and mario_state == 0:
                screen.blit(bigmario_flip[int(mario_count)], (mario_rect.x, mario_rect.y))
            elif mario_size == 2 and mario_state == 0:
                screen.blit(firemario_flip[int(mario_count)], (mario_rect.x, mario_rect.y))
            elif mario_size == 0 and mario_state == 1:
                screen.blit(small_invincible_flip[int(invincible_count)][int(mario_count)], (mario_rect.x,mario_rect.y))
            elif (mario_size == 1 and mario_state == 1) or (mario_size == 2 and mario_state == 1):
                screen.blit(big_invincible_flip[int(invincible_count)][int(mario_count)], (mario_rect.x,mario_rect.y))
        else:
            if (mario_size == 0 and mario_state == 0) or (mario_size == 0 and mario_state == -1):
                screen.blit(animation_list[int(mario_count)], (mario_rect.x,mario_rect.y))
            elif mario_size == 1 and mario_state == 0:
                screen.blit(bigmario_list[int(mario_count)], (mario_rect.x, mario_rect.y))
            elif mario_size == 2 and mario_state == 0:
                screen.blit(firemario_list[int(mario_count)], (mario_rect.x, mario_rect.y))
            elif mario_size == 0 and mario_state == 1:
                screen.blit(small_invincible_list[int(invincible_count)][int(mario_count)], (mario_rect.x,mario_rect.y))
            elif (mario_size == 1 and mario_state == 1) or (mario_size == 2 and mario_state == 1):
                screen.blit(big_invincible_list[int(invincible_count)][int(mario_count)], (mario_rect.x,mario_rect.y))
    else:
        screen.blit(mario_died_pic,(mario_died_x, mario_died_y))

def assign_fireball():
    
    # spawn fireball
    global fireBall_rect_list
    for i in range(len(fireBall_rect_list)): 
        if fireBall_rect_list[i] == None:
            fireBall_rect_list[i] = fireBall_list[i].get_rect(center = mario_rect.center)
            fireball_sound.play()
            break 

def do_fireball():
    # fireball's logics
    global fireBall_rect_list
    global fireBall_vel_y
    global fireBall_vel_x
    global fireBallCount
    global direction
    # animation
    fireBallCount += 0.1
    if fireBallCount > 3: 
        fireBallCount = 0

    for i in range(len(fireBall_rect_list)): 
        if fireBall_rect_list[i]:
            collided_goomba = collide_goomba(fireBall_rect_list[i]) # hit goomba or not 
            collided_wall = check_collisonsx(temp_fireball_rect=fireBall_rect_list[i]) # hit wall or not

            if collided_goomba:
                fireExploded[i] = (collided_goomba.left + bg_x_pos, fireBall_rect_list[i].y)
                fireBall_rect_list[i] = None
            elif collided_wall:
                fireExploded[i] = (collided_wall.left, fireBall_rect_list[i].y)
                fireBall_rect_list[i] = None
            else:
                # hit nothing
                screen.blit(fireBall_list[int(fireBallCount)], fireBall_rect_list[i])
                fireBall_rect_list[i].x += fireBall_vel_x 
                if fireBall_rect_list[i].bottom >= 398: # touches the ground
                    fireBall_vel_y = -4 
                elif fireBall_rect_list[i].bottom <= 376: 
                    fireBall_vel_y = 4
                fireBall_rect_list[i].y += fireBall_vel_y
                # ~ Out of screen
                if fireBall_rect_list[i].x >= 1000 or fireBall_rect_list[i].x <= 0:
                    fireBall_rect_list[i] = None

def fireball_explode(i):
    # Fireball exploding logics
    global fireExploded
    global fireHitCount
    global temp_counter

    fireHitCount += 0.1
    if fireHitCount > 2:
        fireHitCount = 0
    screen.blit(fireHit_animation[int(fireHitCount)], fireExploded[i])
    temp_counter += 1 
    if temp_counter == 25:
        temp_counter = 0
        fireExploded[i] = None

def troll_goomba(rect_):
    global enemy_list
    global goomba_animation_list
    global troller

    foo = None
    for i, goomba_i in enumerate(enemy_list):
        if rect_.colliderect(goomba_i):
            mushroom_list.remove(rect_)
            powerup_eat_sound.play()
            troller = True
            goomba_animation_list[0] = pygame.transform.scale(goomba_animation_list[0], (64, 64))
            goomba_animation_list[1] = pygame.transform.scale(goomba_animation_list[1], (64, 64))
            foo = True
        if foo == True:
            enemy_list[i] = goomba_animation_list[0].get_rect(topleft = (enemy_list[i].left, 334))
def do_goomba():
    
    # goomba's moving and blitting
    global enemy_list
    global enemy_list_alive
    global goomba_animation_i
    global bg_x_pos
    global goomba_ticks

    # goomba move
    for i, goomba_i in enumerate(enemy_list):
        # need to change goomba_alive to goomba_i.alive
        if (enemy_list_alive[i] == True) and (abs(goomba_i.x - abs(bg_x_pos)) <= 1000):
            goomba_i.x -= 1
        # goomba animation
        goomba_animation_i += 0.005
        if goomba_animation_i >= 2:
            goomba_animation_i = 0

        if (abs(goomba_i.x - abs(bg_x_pos)) <= 0):
            # remove them so as to increase the game's performance 
            # no need to process unnecessary information
            enemy_list.remove(goomba_i)
            enemy_list_alive.pop(i)

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

def collide_goomba(rect_ = mario_rect):
    # check if things collided with goomba
    global enemy_list
    global jump
    global on_ground
    global enemy_list_alive
    global mario_state
    global temp_invincible
    global mario_size
    global mario_temp_inv_effect
    global max_height
    global mario_dead

    for i, goomba_i in enumerate(enemy_list):
        if rect_ == mario_rect: # checking collision between mario and goomba
            if (colliderect_on_bg(rect_, goomba_i) and (on_ground == False)) == True:
                if enemy_list_alive[i] == True:
                    stomp_sound.play()
                    if mario_state != 1:
                        # dont bounce if mario is invincible
                        jump = True
                        max_height = goomba_i.bottom - 50 # bounce mario
                    update_score(100)
                    enemy_list_alive[i] = False
            elif (colliderect_on_bg(rect_, goomba_i) and enemy_list_alive[i]) == True:
                if enemy_list_alive[i] == True:
                    if (mario_size == 1 and mario_state != 1) or (mario_size == 2 and mario_state != 1):
                        mario_shrink()
                        mario_state = -1 # temp invincible
                        temp_invincible = pygame.time.get_ticks()
                        pipe_sound.play() # somehow it's pipe sound lol
                    elif mario_state == 0:
                        mario_dead = True
                    elif mario_state == 1:
                        update_score(100)
                        mario_kick_sound.play() 
                        enemy_list_alive[i] = False 

            mario_after_invincible_time = pygame.time.get_ticks()
        
            # ~ Temporary invincible after big mario shrinked
            if temp_invincible: 
                mario_temp_inv_effect += 1 
                if mario_temp_inv_effect == 50:
                    mario_size = 99999 # doesn't exist, so the game won't blit
                                    # thus creating the invincible effect
                    mario_temp_inv_effect = 0
                elif mario_temp_inv_effect == 25: 
                    mario_size = 0
                if mario_after_invincible_time - temp_invincible >= 2000:
                    if mario_state != 1: 
                        mario_state = 0
                    elif mario_state == 1: # ate a star while in this interval
                        mario_state = 1
                    temp_invincible = 0
                    mario_size = 0
                    mario_temp_inv_effect = 0

        else: #rect is other things like fireball
            if (colliderect_on_bg(rect_, goomba_i)):
                if enemy_list_alive[i] == True:
                    stomp_sound.play()
                    update_score(100)
                    enemy_list_alive[i] = False
                    return enemy_list[i]

def check_mario_dead():
    # ~ Mario dead logic 
    global mario_dead
    global time_value
    global mario_rect
    global mario_died_one_time
    global mario_died_x
    global mario_died_y
    global mario_dead_velo
    global seconds
    global after_life_time

    if mario_dead == False:
        # timer to decrease the 400 times 
        # in Mario, 1 sec is 0.6 sec in real life 
        if mario_rect.y >= 448:
            mario_dead = True
        seconds=(pygame.time.get_ticks()-time_ticks)/600
        if (time_value - int(seconds)) <= 0:
            mario_dead = True
    else:
        # these are the things that only have to 
        # happen ONE TIME after mario died
        if mario_died_one_time == False:
            # pause all other musics
            after_life_time = pygame.time.get_ticks()
            mario_died_x = mario_rect.x
            mario_died_y = mario_rect.y
            mario_died_one_time = True
            mario_dead_sound.play()
        # ~ Let Mario jumps when he dies 
        if mario_died_y <= 272:
            mario_dead_velo = 3
        mario_died_y += mario_dead_velo
        restart_game()


while True:

    check_pole()
    draw_floor() #draw the floor before the BG 
    screen.blit(bg, (bg_x_pos,0)) #draw BG 
    #  ~ Flag
    draw_on_bg(pole, rect = pole_rect)
    draw_on_bg(pole_ball, pole_ball_co)
    flag_animation_i += 0.1
    if flag_animation_i >= 10:
        flag_animation_i = 0
    flag_co = (6283, (flag_y_pos))
    draw_on_bg(flag_animation_list[int(flag_animation_i)], flag_co)

    mario_bg_music()

    check_mario_dead()

    collide_goomba(mario_rect)

    draw_on_bg(titleBanner, (37.5, 75)) 
    draw_on_bg(copywrite, (200, 250))

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
    if troller:
        update_score(-1)
    # Coin brick - draw coin
    if colliderect_on_bg_bottom(mario_rect, coin_brick_rect):
        count_coin += 1
        # Only draw coin for the first time of collision
        if count_coin == 1:     
            start_time_coin = pygame.time.get_ticks()      
            
        if start_time_coin:
            coin_time_taken = pygame.time.get_ticks() - start_time_coin
            if coin_time_taken <= 4000:
                coin_sound.play()
                update_coins()
                update_score(200)
                draw_coin = True
                m = 1
                v = 5
            else:
                draw_empty_brick = True 
            
    if draw_coin:
        draw_on_bg(coin, rect = coin_rect0)

        # Let the coin jump
        F = (1/2) * m * (v ** 2) 
        coin_rect0.y -= F
        v -= 0.25
        if v < 0:
            m = -1

        if coin_rect0.y > coin_brick_rect.y:
            draw_coin = False
            
    if draw_empty_brick:
        # Draw empty brick after 4 seconds of the first collsion
        draw_on_bg(empty_brick, rect = coin_brick_rect)
    else:
        # Draw coin brick
        draw_on_bg(brick, rect = coin_brick_rect)
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
        if invincible_music_played == False:
            invincible_music_played = True
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
            if invincible_music_played == True:
                invincible_music_played = False
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
                # Q is fireball 
                if event.key == pygame.K_q:
                    if mario_size == 2:
                        assign_fireball()
            
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
                if mario_size == 0:
                    small_jump_sound.play()
                elif mario_size == 1 or mario_size == 2:
                    big_jump_sound.play()
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
    do_goomba()
    collide_goomba(mario_rect)
    blit_mario()
    do_fireball()
    for i in range(len(fireExploded)):
        if fireExploded[i]:
            fireball_explode(i)

    #### #### #### #### #### RAJA's end #### #### #### #### #### ####

    if debris_list["DEBRIS"]:
        draw_debris()
    
    if lives_value < 0:
        game_over_screen()
    display_top_texts()
    pygame.display.update()  #update screen
    delta_time = clock.tick(TARGET_FPS) * 0.001 * TARGET_FPS  #clock.tick(FPS) limit our game to 60 fps no matter what
