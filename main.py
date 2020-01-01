import pygame
import sumHelper
import raceHelper
import car

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

# initial setup
player1 = car.Car('Player 1')
player2 = car.Car('Player 2')
# set player2 to appear below player1
player2.set_position(player2.x, player1.y+50)

currentPlayer = player1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # fetch asum for the current player

    # set the x/y based on sum answer


    # fill screen white
    screen.fill((255, 255, 255))

    # draw start and finsih lines



    # divide between lines into x segments



    # draw players


    pygame.display.flip()
    pygame.time.clock.tick(60)

    # has a player won?

    # toggle current player
    if currentPlayer == player1:
        currentPlayer = player2
    else:
        currentPlayer = player1