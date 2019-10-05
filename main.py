import sys
from config import gameConfig as config
import pygame
import random
import sumHelper
import raceHelper

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

x = 30
y = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

    # select number of players

    # select difficultly if one player

    # select track size

    # start game loop

