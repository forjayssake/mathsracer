import pygame
import os

# it is better to have an extra variable, than an extremely long line.
img_path = os.path.join('{python path}}', 'car.png')

class Car(object):

    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load(img_path)
        # starting position
        self.x = 5
        self.y = 350

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))