import pygame

player_image = pygame.image.load('assets/images/player.png').convert_alpha()

player_images = {'right' : player_image,
                 'left' : pygame.transform.flip(player_image, True, False)}

box_image = pygame.image.load('assets/images/blocks/box.png').convert_alpha()

ground_image = pygame.image.load('assets/images/blocks/ground.png').convert_alpha()

sand_image = pygame.image.load('assets/images/blocks/sand.png').convert_alpha()

water_image = pygame.image.load('assets/images/blocks/water.png').convert_alpha()

stop_image = pygame.image.load('assets/images/blocks/stop.png').convert_alpha()

enemy1_image = pygame.image.load('assets/images/enemy/1/1.png').convert_alpha()

enemy2_image = pygame.image.load('assets/images/enemy/2/1.png').convert_alpha()

enemy3_image = pygame.image.load('assets/images/enemy/3/1.png').convert_alpha()

portal1_image = pygame.image.load('assets/images/portal/portal1.png').convert_alpha()


































