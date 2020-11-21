import pygame
import random


class White(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('anxiety.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000)
        self.rect.y = random.randint(0, 500)
        self.velocity = 1
        self.score = 0

    def more_points(self):
        self.score = self.score + 1
        print("Ton score est de : ", self.score)


















