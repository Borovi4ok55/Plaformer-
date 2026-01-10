import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step, player_group, player):
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

    def update(self, step, player_group, player):
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

    def update(self, step, player_group, player):
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

    def update(self, step, player_group, player):
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

    def update(self, player_images, scroll_group,  player_group, player):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            # self.image = pygame.transform.flip(player_image, False, False)
            self.image = player_images['right']
            self.rect.x += self.speed
            if self.rect.right > 800:
                self.rect.right = 800
                scroll_group.update(-self.speed, player_group, player)
        if key[pygame.K_LEFT]:
            # self.image = pygame.transform.flip(player_image, True, False)
            self.image = player_images['left']
            self.rect.x -= self.speed
            if self.rect.left < 200:
                self.rect.left = 200
                scroll_group.update(self.speed,  player_group, player)
        if key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10