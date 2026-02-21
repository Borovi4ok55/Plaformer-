import pygame
import sys
import random

import pygwidgets

from sprites.spriteclasses import *

GREY = (210, 210, 210)
WIDTH = 1200
HEIGHT = 800
FPS = 60
HP_BAR_WIDTH = 300
HP_BAR_HEIGHT = 30
HP_BAR_X = 200
HP_BAR_Y = 20


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()



from load import *

def restart():
    global box_group, ground_group, player_group, scroll_group,\
        sand_group, water_group, player, enemy_group, coin_group, stopenemy_group, portal_group, \
        hp, hp_text, color, hpbott_group
    box_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    sand_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    scroll_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    stopenemy_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    hpbott_group = pygame.sprite.Group()

    player = Player(player_image,(480, 560))
    player_group.add(player)

    color = (0,200,0)
    hp = 100
    hp_text = pygwidgets.DisplayText(window,(200,20), 'HP: 100',
                                     fontSize=40, textColor=(0,0,0))



def lvlGame():
    global box_group, ground_group, step, player_group, sand_group,\
        water_group, player, enemy_group, coin_group, stopenemy_group, portal_group,\
        hp, hp_text, color, hpbott_group
    step = 0
    box_group.draw(window)
    ground_group.draw(window)
    water_group.draw(window)
    sand_group.draw(window)
    player_group.draw(window)
    enemy_group.draw(window)
    coin_group.draw(window)
    portal_group.draw(window)
    hpbott_group.draw(window)

    pygame.draw.rect(window, (150, 150, 150),
                     (HP_BAR_X, HP_BAR_Y, HP_BAR_WIDTH, HP_BAR_HEIGHT))
    current_width = (hp / 100) * HP_BAR_WIDTH
    pygame.draw.rect(window, color,
                     (HP_BAR_X, HP_BAR_Y, current_width, HP_BAR_HEIGHT))
    pygame.draw.rect(window, (0, 0, 0),
                     (HP_BAR_X, HP_BAR_Y, HP_BAR_WIDTH, HP_BAR_HEIGHT), 2)
    hp_text.draw()
    box_group.update(step, player_group, player, stopenemy_group)
    ground_group.update(step, player_group, player, stopenemy_group)
    water_group.update(step, player_group, player, stopenemy_group)
    sand_group.update(step, player_group, player, stopenemy_group)
    player_group.update(player_images, scroll_group,  player_group, player, stopenemy_group, FPS)
    enemy_group.update(step, player_group, player, stopenemy_group, )
    coin_group.update(step, player_group, player, stopenemy_group)
    stopenemy_group.update(step, player_group, player, stopenemy_group)
    # portal_group.update(step, player_group, player, stopenemy_group)
    hpbott_group.update(step, player_group, player, stopenemy_group)
    for enemy in enemy_group:
        enemy.move(FPS, enemy1_image, stopenemy_group)
    if player.rect.y > 850:
        player.kill()
        restart()
        drawMap('game_lvl/lvl1.csv')
    hit_enemies = pygame.sprite.spritecollide(player, enemy_group, False)
    for enemy in hit_enemies:
        if player.velocity_y > 0 and \
            player.rect.bottom - enemy.rect.top < 20:
            enemy.kill()
        else:
            if not player.invulnerable:
                hp -= 10
                player.invulnerable = True
                hp_text.setValue(f'HP:{hp}')
        if hp <= 0:
            player.kill()
            restart()
            drawMap('game_lvl/lvl1.csv')
            return



    if pygame.sprite.spritecollide(player, hpbott_group, True):
        hp += 30
        if hp > 100:
            hp = 100
        hp_text.setValue(f'HP:{hp}')

    if hp > 60:
        color = (0, 200, 0)
    elif hp > 30:
        color = (255, 165, 0)
    elif hp <= 30:
        color = (200, 0, 0)





    pygame.display.update()

def drawMap(mapFile):
    global box_group, ground_group, step, player_group, sand_group, \
        water_group, player, enemy_group, coin_group, stopenemy_group, portal_group
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
            elif game_map[i][j] == '4':
                coin = Coin(coin_image, pos)
                coin_group.add(coin)
                scroll_group.add(coin)
            elif game_map[i][j] == '5':
                stopenemy = StopEnemy(stop_image, pos)
                stopenemy_group.add(stopenemy)
                scroll_group.add(stopenemy)
            elif game_map[i][j] == '6':
                enemy1 = Enemy(enemy1_image[0], pos)
                enemy_group.add(enemy1)
                scroll_group.add(enemy1)
            elif game_map[i][j] == '7':
                enemy2 = Enemy(enemy2_image, pos)
                enemy_group.add(enemy2)
                scroll_group.add(enemy2)
            elif game_map[i][j] == '8':
                enemy3 = Enemy(enemy3_image, pos)
                enemy_group.add(enemy3)
                scroll_group.add(enemy3)
            elif game_map[i][j] == '9':
                enemy4 = Enemy(enemy4_image, pos)
                enemy_group.add(enemy4)
                scroll_group.add(enemy4)
            elif game_map[i][j] == '10':
                portal1 = Portal(portal1_image, pos)
                portal_group.add(portal1)
                scroll_group.add(portal1)
            elif game_map[i][j] == '11':
                hpbott = HpBott(hpbott_image, pos)
                hpbott_group.add(hpbott)
                scroll_group.add(hpbott)


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





























































































