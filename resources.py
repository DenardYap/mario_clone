import pygame
import sys

pygame.init()

# General           #x   y   w    h 
floor1 = pygame.Rect(0, 400, 2207, 50)
floor2 = pygame.Rect(2272, 400, 480, 50)
floor3 = pygame.Rect(2847, 400, 2048, 50)
floor4 = pygame.Rect(4960, 400, 2140, 50)
floor_list = [floor1, floor2, floor3, floor4]
bg = pygame.image.load("static_images/background.png")
mario = pygame.image.load("static_images/mario.png")
mario_rect = mario.get_rect(topleft = (40, 368))

#pole
pole = pygame.image.load("static_images/pole.png")
pole_ball = pygame.image.load("static_images/pole_ball.png")
pole_ball_co = (6341, 77)
pole_rect = pole.get_rect(bottomleft = (6347, 368))
#fonts
SCORE = "SCORE"
COINS = "COINS"
WORLD = "WORLD"
TIME = "TIME"
LIVES = "LIVES"
WHITE = (255,255,255)
mario_font = pygame.font.Font("fonts/mario_font.ttf", 36)
score_font = mario_font.render(SCORE, False, WHITE)
coins_font = mario_font.render(COINS, False, WHITE)
world_font = mario_font.render(WORLD, False, WHITE)
time_font = mario_font.render(TIME, False, WHITE)
lives_font = mario_font.render(LIVES, False, WHITE)

#pipe
small_pipe = pygame.image.load("static_images/pipe_small.png")
medium_pipe = pygame.image.load("static_images/pipe_medium.png")
long_pipe = pygame.image.load("static_images/pipe_long.png")
pipe1_rect = small_pipe.get_rect(bottomleft = (896,400))
pipe2_rect = medium_pipe.get_rect(bottomleft = (1216,400))
pipe3_rect = long_pipe.get_rect(bottomleft = (1472,400))
pipe4_rect = long_pipe.get_rect(bottomleft = (1824,400))
pipe5_rect = small_pipe.get_rect(bottomleft = (5216,400))
pipe6_rect = small_pipe.get_rect(bottomleft = (5728,400))

### YUN SION's ###

titleBanner = pygame.image.load('static_images/title.png')
main_theme_song = pygame.mixer.Sound('music/main_theme.ogg')
game_over_song = pygame.mixer.Sound('music/game_over.ogg')
font = pygame.font.Font('fonts/mario_font.ttf', 24) 
gameoverFont = pygame.font.Font('fonts/mario_font.ttf', 72) 
copywrite = font.render("©1985 Nintendo", False ,(255,255,0))
gameoverText = gameoverFont.render("GAME OVER", False, (255,255,255))
gameoverText_rect = gameoverText.get_rect(center=(500,224))

mario_dead_sound = pygame.mixer.Sound("music/dead.wav")
mario_died_pic = pygame.image.load("static_images/mario_died.png")

### BEN's ###

goomba_animation_list = []
goomba_animation_list.append(pygame.image.load("./animate_images/goomba0.png"))
goomba_animation_list.append(pygame.image.load("./animate_images/goomba1.png"))
goomba_hitbox = goomba_animation_list[0].get_rect(topleft = (700, 448-48-32))
goomba_death_ani = pygame.image.load("./static_images/goomba_died.png")

enemy_list = [goomba_hitbox]
#############

### EEJOY's ### 

# Import brick
brick = pygame.image.load("static_images/brick.png")
brick_rect1 = brick.get_rect(topleft = (640, 272))
brick_rect2 = brick.get_rect(topleft = (704, 272))
brick_rect3 = brick.get_rect(topleft = (768, 272))
brick_rect4 = brick.get_rect(topleft = (2462, 272))
brick_rect5 = brick.get_rect(topleft = (2526, 272))
brick_rect6 = brick.get_rect(topleft = (2559, 144))
brick_rect7 = brick.get_rect(topleft = (2591, 144))
brick_rect8 = brick.get_rect(topleft = (2623, 144))
brick_rect9 = brick.get_rect(topleft = (2655, 144))
brick_rect10 = brick.get_rect(topleft = (2687, 144))
brick_rect11 = brick.get_rect(topleft = (2719, 144))
brick_rect12 = brick.get_rect(topleft = (2751, 144))
brick_rect13 = brick.get_rect(topleft = (2783, 144))
brick_rect14 = brick.get_rect(topleft = (2911, 144))
brick_rect15 = brick.get_rect(topleft = (2943, 144))
brick_rect16 = brick.get_rect(topleft = (2975, 144))
brick_rect17 = brick.get_rect(topleft = (3199, 272))
brick_rect18 = brick.get_rect(topleft = (3774, 272))
brick_rect19 = brick.get_rect(topleft = (3871, 144))
brick_rect20 = brick.get_rect(topleft = (3903, 144))
brick_rect21 = brick.get_rect(topleft = (3935, 144))
brick_rect22 = brick.get_rect(topleft = (4095, 144))
brick_rect23 = brick.get_rect(topleft = (4159, 144))
brick_rect24 = brick.get_rect(topleft = (4191, 144))
brick_rect25 = brick.get_rect(topleft = (4127, 272))
brick_rect26 = brick.get_rect(topleft = (4159, 272))
brick_rect27 = brick.get_rect(topleft = (5374, 272))
brick_rect28 = brick.get_rect(topleft = (5406, 272))
brick_rect29 = brick.get_rect(topleft = (5470, 272))
coin_brick_rect = brick.get_rect(topleft = (3007, 272))
star_brick_rect = brick.get_rect(topleft = (3231, 272))
remove_coin_list = []
remove_mushroom_list = []
# maybe can come out with a better name as this list
# does both Draw and Remove
remove_flower_list = []
# maybe can come out with a better name as this list
# does both Draw and Remove
remove_brick_list = []
drawn_mushroom_list = []
drawn_flower_list = []
empty_brick_list = []

# import rocks
rock_rect1 = pygame.Rect(4286, 368, 32, 32)
rock_rect2 = pygame.Rect(4318, 336, 32, 32)
rock_rect3 = pygame.Rect(4350, 304, 32, 32)
rock_rect4 = pygame.Rect(4382, 272, 32, 32)
rock_rect4_1 = pygame.Rect(4382, 304, 32, 32)
rock_rect4_2 = pygame.Rect(4382, 336, 32, 32)
rock_rect4_3 = pygame.Rect(4382, 368, 32, 32)
rock_rect5 = pygame.Rect(4477,  272, 32, 32)
rock_rect5_1 = pygame.Rect(4477,  304, 32, 32)
rock_rect5_2 = pygame.Rect(4477,  336, 32, 32)
rock_rect5_3 = pygame.Rect(4477,  368, 32, 32)
rock_rect6 = pygame.Rect(4509,  304, 32, 32)
rock_rect7 = pygame.Rect(4541,  336, 32, 32)
rock_rect8 = pygame.Rect(4573,  368, 32, 32)
rock_rect9 = pygame.Rect(4734,  368, 32, 32)
rock_rect10 = pygame.Rect(4766,  336, 32, 32)
rock_rect11 = pygame.Rect(4798, 304, 32, 32)
rock_rect12 = pygame.Rect(4830, 272, 32, 32)
rock_rect13 = pygame.Rect(4862, 272, 32, 32)
rock_rect13_1 = pygame.Rect(4862, 304, 32, 32)
rock_rect13_2 = pygame.Rect(4862, 336, 32, 32)
rock_rect13_3 = pygame.Rect(4862, 368, 32, 32)
rock_rect14 = pygame.Rect(4957, 272, 32, 32)
rock_rect14_1 = pygame.Rect(4957, 304, 32, 32)
rock_rect14_2 = pygame.Rect(4957, 336, 32, 32)
rock_rect14_3 = pygame.Rect(4957, 368, 32, 32)
rock_rect15 = pygame.Rect(4989, 302, 32, 32)
rock_rect16 = pygame.Rect(5020, 336, 32, 32)
rock_rect17 = pygame.Rect(5052, 368, 32, 32)
rock_rect18 = pygame.Rect(5790, 368, 32, 32)
rock_rect19 = pygame.Rect(5822, 336, 32, 32)
rock_rect20 = pygame.Rect(5854, 304, 32, 32)
rock_rect21 = pygame.Rect(5886, 272, 32, 32)
rock_rect22 = pygame.Rect(5918, 240, 32, 32)
rock_rect23 = pygame.Rect(5950, 208, 32, 32)
rock_rect24 = pygame.Rect(5982, 176, 32, 32)
rock_rect25 = pygame.Rect(6014, 144, 32, 32)
rock_rect26 = pygame.Rect(6046, 144, 32, 32)
rock_rect26_1 = pygame.Rect(6046, 176, 32, 32)
rock_rect26_2 = pygame.Rect(6046, 208, 32, 32)
rock_rect26_3 = pygame.Rect(6046, 240, 32, 32)
rock_rect26_4 = pygame.Rect(6046, 272, 32, 32)
rock_rect26_5 = pygame.Rect(6046, 304, 32, 32)
rock_rect26_6 = pygame.Rect(6046, 336, 32, 32)
rock_rect26_7 = pygame.Rect(6046, 368, 32, 32)
rock_rect27 = pygame.Rect(6333, 368, 32, 32)
# Import coin
coin = pygame.image.load("static_images/coin.png")
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
question_rect9 = question_block[0].get_rect(topleft = (5438, 272))

# Mushroom box
question_rect10 = question_block[0].get_rect(topleft = (672, 272))
question_rect11 = question_block[0].get_rect(topleft = (2494, 272))
question_rect12 = question_block[0].get_rect(topleft = (3486, 144))

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

# Import star
star = []
star.append(pygame.image.load("animate_images/star0.png"))
star.append(pygame.image.load("animate_images/star1.png"))
star.append(pygame.image.load("animate_images/star2.png"))
star.append(pygame.image.load("animate_images/star3.png"))
star_rect = star[0].get_rect(topleft = (3231, 270))

# Import flower
flower = []
flower.append(pygame.image.load("animate_images/flower0.png"))
flower.append(pygame.image.load("animate_images/flower1.png"))
flower.append(pygame.image.load("animate_images/flower2.png"))
flower.append(pygame.image.load("animate_images/flower3.png"))
flower_rect1 = flower[0].get_rect(topleft = (672, 270))
flower_rect2 = flower[0].get_rect(topleft = (2494, 270))
flower_rect3 = flower[0].get_rect(topleft = (3486, 142))

# Import small invincible
a = [pygame.image.load("animate_images/small_invincible1_0.png"), pygame.image.load("animate_images/small_invincible2_0.png"), 
    pygame.image.load("animate_images/small_invincible3_0.png"), pygame.image.load("animate_images/small_invincible2_0.png"),
    pygame.image.load("animate_images/small_invincible0_0.png"), pygame.image.load("animate_images/small_invincible_jump0_0.png")]
b = [pygame.image.load("animate_images/small_invincible1_1.png"), pygame.image.load("animate_images/small_invincible2_1.png"), 
    pygame.image.load("animate_images/small_invincible3_1.png"), pygame.image.load("animate_images/small_invincible2_1.png"),
    pygame.image.load("animate_images/small_invincible0_1.png"), pygame.image.load("animate_images/small_invincible_jump0_1.png")]
c = [pygame.image.load("animate_images/small_invincible1_2.png"), pygame.image.load("animate_images/small_invincible2_2.png"), 
    pygame.image.load("animate_images/small_invincible3_2.png"), pygame.image.load("animate_images/small_invincible2_2.png"),
    pygame.image.load("animate_images/small_invincible0_2.png"), pygame.image.load("animate_images/small_invincible_jump0_2.png")]

small_invincible_list = [a, b, c]

a_flip = []
for i,small_invincible in enumerate(a):
    a_flip.append(pygame.transform.flip((a[i]), True, False))
b_flip = []
for i,small_invincible in enumerate(b):
    b_flip.append(pygame.transform.flip((b[i]), True, False))
c_flip = []
for i,small_invincible in enumerate(c):
    c_flip.append(pygame.transform.flip((c[i]), True, False))

small_invincible_flip = [a_flip, b_flip, c_flip]

###############
#Mario animation
animation_list = []
animation_list.append(pygame.image.load("animate_images/mario0.png"))
animation_list.append(pygame.image.load("animate_images/mario1.png"))
animation_list.append(pygame.image.load("animate_images/mario2.png"))
animation_list.append(pygame.image.load("animate_images/mario1.png"))
animation_list.append(pygame.image.load("static_images/mario.png"))
animation_list.append(pygame.image.load("static_images/mario_jump.png"))    

marioflip = []
for i,animation in enumerate(animation_list):
    marioflip.append(pygame.transform.flip((animation_list[i]), True, False))

#sounds
big_jump_sound = pygame.mixer.Sound('sounds/big_jump.ogg')
small_jump_sound = pygame.mixer.Sound('sounds/small_jump.ogg')
small_jump_sound.set_volume(0.5)
main_theme_speedup = pygame.mixer.Sound('music/main_theme_speed_up.ogg')
brick_smash_sound = pygame.mixer.Sound('sounds/brick_smash.ogg')
bump_sound = pygame.mixer.Sound('sounds/bump.ogg')
coin_sound = pygame.mixer.Sound('sounds/coin.ogg')
powerup_pop_sound = pygame.mixer.Sound('sounds/powerup_pop.ogg')
powerup_eat_sound = pygame.mixer.Sound('sounds/powerup_eat.ogg')
mario_kick_sound = pygame.mixer.Sound('sounds/kick.ogg')
invincible_music = pygame.mixer.Sound('music/invincible.ogg')

