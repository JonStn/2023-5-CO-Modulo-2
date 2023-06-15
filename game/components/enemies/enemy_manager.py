import pygame
import random

from game.utils.constants import ENEMY_1, ENEMY_2
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy_type = random.choice([ENEMY_1, ENEMY_2])
            if enemy_type == ENEMY_1:
                enemy = Enemy(ENEMY_1, 40, 60, 3, 5, 30, 70)
            elif enemy_type == ENEMY_2:
                enemy = Enemy(ENEMY_2, 30, 40, 12 , 3, 50, 100)
            self.enemies.append(enemy)