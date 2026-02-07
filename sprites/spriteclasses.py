import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step, player_group, player, stopEnemy_group):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if abs(self.rect.left - player.rect.right) < 15 \
                and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left



class Sand(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step, player_group, player, stopEnemy_group):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(player.rect.right - self.rect.left ) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.left = self.rect.right


class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step, player_group, player, stopEnemy_group):
        self.rect.x += step
        # if pygame.sprite.spritecollide(self, player_group, False):
        #     if abs(self.rect.top - player.rect.bottom) < 15:
        #         player.rect.bottom = self.rect.top - 5
        #         player.on_ground = True
        #     if abs(self.rect.bottom - player.rect.top) < 15:
        #         player.rect.top = self.rect.bottom + 5
        #         player.velocity_y = 0
        #     if abs(self.rect.left - player.rect.right) < 15 \
        #             and abs(self.rect.centery - player.rect.centery) < 50:
        #         player.rect.right = self.rect.left
        #     if abs(player.rect.right - self.rect.left ) < 15 \
        #             and abs(self.rect.centery - player.rect.centery) < 50:
        #         player.rect.left = self.rect.right


class Box(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step, player_group, player, stopEnemy_group):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs( self.rect.right - player.rect.left) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.left = self.rect.right


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5
        self.velocity_y = 0
        self.on_ground = True
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def animation(self, player_images, FPS):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.05:
                if self.frame == len(player_images) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def update(self, player_images, scroll_group,  player_group, player, stopEnemy_group, FPS):
        self.animation(self, player_images, FPS)
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.anime = True
            # self.image = pygame.transform.flip(player_image, False, False)
            self.image = player_images[self.frame]
            self.rect.x += self.speed
            if self.rect.right > 800:
                self.rect.right = 800
                scroll_group.update(-self.speed, player_group, player, stopEnemy_group)
        elif key[pygame.K_LEFT]:
            self.anime = True
            self.image = pygame.transform.flip(player_images[self.frame], True, False)
            # self.image = player_images['left']
            self.rect.x -= self.speed
            if self.rect.left < 200:
                self.rect.left = 200
                scroll_group.update(self.speed,  player_group, player, stopEnemy_group)
        else:
            self.anime = False
        if key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10





class Portal(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step, player_group, player, stopeEnemy_group):
        self.rect.x += step


class Coin(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step, player_group, player, stopEnemy_group):
        self.rect.x += step


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = 1

    def update(self, step, player_group, player, stopEnemy_group):
        self.rect.x += step
        if self.dir == 1:
            self.image = pygame.transform.flip(self.image, False, False)
            self.rect.x += self.speed
        elif self.dir == -1:
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self, stopEnemy_group, False):
            self.dir = -self.dir





class StopEnemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step, player_group, player, stopEnemy_group):
        self.rect.x += step

