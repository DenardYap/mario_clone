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

pygame.init()
screen=pygame.display.set_mode((1000,448))
clock = pygame.time.Clock()

# import images & animation here
# Tips: The bricks (floor) is 48px height

# import sounds here
game_over_sound = pygame.mixer.Sound(r'music/game_over.ogg')

# import fonts here
font = pygame.font.Font(r'fonts/mario_font.ttf', 72) 
gameoverText = font.render("GAME OVER", False, (255,255,255))
gameoverText_rect = gameoverText.get_rect(center=(500,224))


while True:

    #game over screen
    screen.fill((0,0,0))
    screen.blit(gameoverText,gameoverText_rect)
    game_over_sound.play(loops=0,maxtime=0,fade_ms=0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_sound.stop()
            pygame.mixer.quit
            sys.exit()
    pygame.display.update()
    clock.tick(60) #limit our game to 60 fps no matter what
