
### NAZRIN's ### 
screenW = 1000
screenH = 448
marioW = 24    #mario width
marioH = 32    #mario height
bg_x_pos = 0   #background position
bgW = 6784     #bacgkround width
bgH = 448      #background height
mario_x_pos = 0
mario_y_pos = 368
marioWalkR =  False
marioWalkL = False
bgLimit = screenW - bgW
bglimitH = screenH - bgH
# marioSpeed = 10


### YUN SION's ###
mario_dead = False
mario_died_one_time = False
mario_died_x = 0
mario_died_y = 0
mario_dead_velo = -3

### EEJOY's ###
mario_speed = 5.0
question_count = 0
flower_count = 0

draw_coin = False
draw_star = False
count_coin = 0
count_star = 0
count_star_rect = 0

vx = 4
vy = 5

m = 1
v = 5

# If small = 0, big = 1
mario_size = 0
# If normal = 0, invincible = 1, fire = 2
mario_state = 0

invincible_count = 0
start_time_invincible = 0
start_time_grow = 0

### BEN's ###
goomba_alive = True
goomba_animation_i = 0

##Darshini's##
BASE = 368 #mario default landing point = floor
x_pos = 50
y_pos = 368
on_ground = True
JUMP_HEIGHT = 128
default_on_ground_y = 400
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
#############

# LUKE's # 
score_value = 0
coins_value = 0
world_value = "1-1"
time_value = 400
lives_value = 3

#sounds
main_theme_play = False
main_theme_fastvers = False
invincible__music = False

# Bernard
acceleration_x = 0
acceleration_vx = 0.025 # v for value
ski_acceleration = 0.04 # PERFECT VALUE!!
maximum_acceleration_x = 1 # counterintuitve to newton's law lol
maximum_velocity = 3
skied_left = True
skied_right = True
# F = 1/2 mv^2
mario_m = -0.5
