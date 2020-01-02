import pygame
import os

class Car(object):

    def __init__(self, displayName, imageName):
        self.name = imageName
        img_path = os.path.join('/home/jay/pycharmProjects/MathsRacer/images/', imageName)
        self.image = pygame.image.load(img_path)
        # starting position
        self.x = 5
        self.y = 350
        self.increment = 50

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))