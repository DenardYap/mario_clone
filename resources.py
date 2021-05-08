import pygame
import sys

pygame.init()

# General 
bg = pygame.image.load("static_images/background.png")
mario = pygame.image.load("static_images/mario.png")
mario_rect = mario.get_rect(topleft = (40, 368))

### YUN SION's ###

titleBanner = pygame.image.load('static_images/title.png')
main_theme_song = pygame.mixer.Sound('music\main_theme.ogg')
game_over_song = pygame.mixer.Sound('music\game_over.ogg')
font = pygame.font.Font('fonts\mario_font.ttf', 24) 
gameoverFont = pygame.font.Font('fonts\mario_font.ttf', 72) 
copywrite = font.render("©1985 Nintendo", False ,(255,255,0))
gameoverText = gameoverFont.render("GAME OVER", False, (255,255,255))
gameoverText_rect = gameoverText.get_rect(center=(500,224))

### BEN's ###

goomba_animation_list = []
goomba_animation_list.append(pygame.image.load("./animate_images/goomba0.png"))
goomba_animation_list.append(pygame.image.load("./animate_images/goomba1.png"))
goomba_hitbox = goomba_animation_list[0].get_rect(topleft = (700, 448-48-32))
goomba_death_ani = pygame.image.load("./static_images/goomba_died.png")

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
brick_rect28 = brick.get_rect(topleft = (5407, 272))
brick_rect29 = brick.get_rect(topleft = (5471, 272))

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

# Import star
star = []
star.append(pygame.image.load("animate_images/star0.png"))
star.append(pygame.image.load("animate_images/star1.png"))
star.append(pygame.image.load("animate_images/star2.png"))
star.append(pygame.image.load("animate_images/star3.png"))
star_rect = star[0].get_rect(midtop = star_brick_rect.midtop)

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

###############
