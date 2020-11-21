import pygame

from circle import Circle
from white import White

class Game:
    def __init__(self):
        self.welcome = True
        self.first_level = False
        self.second_level = False
        self.circle = Circle()
        self.all_circles = pygame.sprite.Group()


        self.white = White()
        self.all_whites = pygame.sprite.Group()




    def level1(self):

        self.first_level = True
        self.spawn_circle()
        self.spawn_white()

    def level2(self):
        self.second_level = True
        self.spawn_circle()

    def update2(self, screen):
        screen.blit(self.white.image, self.white.rect)





    def update(self, screen):

        screen.blit(self.circle.image, self.circle.rect)
        screen.blit(self.white.image, self.white.rect)

    def spawn_circle(self):

        circle = Circle()
        self.all_circles.add(circle)

    def spawn_white(self):
        white = White()
        self.all_whites.add(white)





