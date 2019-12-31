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

    # draw start and finsih lines

    # divide between lines into x segments

    # draw two rectangles before first line


    

    screen.fill((0, 0, 0))

    pygame.display.flip()
    pygame.clock.tick(60)