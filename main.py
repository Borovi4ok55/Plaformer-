import pygame
import sys
import random
from sprites.spriteclasses import *

GREY = (210, 210, 210)
WIDTH = 1200
HEIGHT = 800
FPS = 60

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

from load import *

def restart():
    global box_group, ground_group, player_group, scroll_group, sand_group, water_group, player
    box_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    sand_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    scroll_group = pygame.sprite.Group()

    player = Player(player_image,(480, 560))
    player_group.add(player)

def lvlGame():
    global box_group, ground_group, step, player_group, sand_group, water_group, player
    step = 0
    box_group.draw(window)
    ground_group.draw(window)
    water_group.draw(window)
    sand_group.draw(window)
    player_group.draw(window)
    box_group.update(step, player_group, player)
    ground_group.update(step, player_group, player)
    water_group.update(step, player_group, player)
    sand_group.update(step, player_group, player)
    player_group.update(player_images, scroll_group,  player_group, player)
    if player.rect.y > 850:
        player.kill()
        restart()
        drawMap('game_lvl/lvl1.csv')



    pygame.display.update()

def drawMap(mapFile):
    game_map = []
    with open(mapFile, 'r') as file:
        for i in range(10):
            game_map.append(file.readline().replace('\n', '').split(','))
    pos = [0, 0]
    for i in range(10):
        pos[1] = i * 80
        for j in range(100):
            pos[0] = j * 80
            if game_map[i][j] == '0':
                ground = Ground(ground_image, pos)
                ground_group.add(ground)
                scroll_group.add(ground)
            elif game_map[i][j] == '1':
                sand = Sand(sand_image, pos)
                sand_group.add(sand)
                scroll_group.add(sand)
            elif game_map[i][j] == '2':
                water = Water(water_image, pos)
                water_group.add(water)
                scroll_group.add(water)
            elif game_map[i][j] == '3':
                box = Box(box_image, pos)
                box_group.add(box)
                scroll_group.add(box)

restart()
drawMap('game_lvl/lvl1.csv')


while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()






    window.fill(GREY)
    lvlGame()
    pygame.display.update()





























































































