
### NAZRIN's ### 
screenW = 1000
screenH = 448
marioW = 24    #mario width
marioH = 32    #mario height
bg_x_pos = 0   #background position
bgW = 6784     #bacgkround width
bgH = 448      #background height
bgLimit = screenW - bgW
bglimitH = screenH - bgH
flag_animation_i = 0
play_flag_song = 0
flag_y_pos = 93
end_song = 0
endgame_delay = 0
flag_mario_drop = False
jump_logic = True
bonus_score = 0
play_flag_song = False 
mario_clear_stage = False
marioEndScene = False
win_animation = 0
TARGET_FPS = 60
# marioSpeed = 10


### YUN SION's ###
mario_dead = False
mario_died_one_time = False
mario_died_x = 0
mario_died_y = 0
mario_dead_velo = -3

### EEJOY's ###

question_count = 0
mushroom_count = 0
mushroom_finish_rising = False
mushroom_dropping = False
collided = False
mushroom_vel_x = 1.5
mushroom_vel_y = 3
flower_count = 0
mario_grew = False
draw_coin = False
draw_star = False
count_coin = 0
count_star = 0
count_star_rect = 0
transform_time_taken = 999

vx = 4
vy = 5

m = 1
v = 5

# If small = 0, big = 1, fire = 2
mario_size = 0
# If normal = 0, invincible = 1, temp_invincible = -1
mario_state = 0
bumping_brick = None
bumping_brick_ori_y = 0
bumping_brick_velo_y = -0.5
invincible_count = 0
start_time_invincible = 0
start_time_grow = 0
start_time_coin = 0
draw_empty_brick = False
### BEN's ###

goomba_animation_i = 0

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

goomba_velocity_x_list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
goomba_velocity_y_list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

##Darshini's##
BASE = 368 #mario default landing point = floor
x_pos = 50
y_pos = 368
on_ground = True
JUMP_HEIGHT = 128
default_on_ground_y = 400
max_height = default_on_ground_y - JUMP_HEIGHT
moving_right = False
moving_left = False
mario_count = 0
jump = False
jumpspeed = 10
velocity_x = 0
velocity_y = 6
direction = 0
facing_right = 1
facing_left = -1

#sounds
main_theme_play = False
main_theme_fastvers = False
invincible_music_played = False
###################################

# Bernard
# ~ Physics
acceleration_x = 0
acceleration_vx = 0.025 # v for value
ski_acceleration = 0.04 # PERFECT VALUE!!
maximum_acceleration_x = 1 # counterintuitve to newton's law lol
maximum_velocity = 3
skied_left = True
skied_right = True
# F = 1/2 mv^2
mario_m = -0.5

# ~ Debris

debris_list = {"DEBRIS": [], "Y": [],
               "BL": [], "BR": [], 
               "TL": [], "TR": []}
debris_vx = 3
debris_vy = -4

# ~ Top texts
score_value = 0
coins_value = 0
world_value = "1-1"
time_value = 400
lives_value = 3
seconds = 0

# ~ temporary invincible 
temp_invincible = 0
mario_temp_inv_effect = 0

# ~ afterlife
after_life_time = 0
BLACK = (0, 0, 0)
game_over_song_played = False
game_over_song_timer = 0

# Fireball 
fireBallCount = 0 # max = 3
fireHitCount = 0 # max = 2
fireBall_vel_x = 8
fireBall_vel_y = 4
temp_counter = 0

# Troll
troller = False
