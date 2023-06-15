import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(Sprite):
    Y_POS = 20
    MOV_X = {0: 'left', 1: 'right'}

    def __init__(self, IMAGE, ENEMY_WIDTH, ENEMY_HEIGHT, SPEED_X, SPEED_Y, MIN_MOVE, MAX_MOVE):
        self.image = pygame.transform.scale(IMAGE, (ENEMY_WIDTH,ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
        self.rect.y = self.Y_POS
        self.speed_x = SPEED_X
        self.speed_y = SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(MIN_MOVE, MAX_MOVE)
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = random.randint(30, 50)
    
    
    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        for bullet in game.bullet_manager.bullets:
            if bullet.rect.colliderect(self.rect) and bullet.owner == 'player':
                if self in ships:
                    ships.remove(self)

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.rect.width):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0
    
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)
    