import pygame
import sumHelper
import raceHelper
import car

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Maths Racer!')
clock = pygame.time.Clock()
done = False

# initial setup
player1 = car.Car('Player 1', 'car_1.png')
player2 = car.Car('Player 2', 'car_2.png')
# set player2 to appear below player1
player2.set_position(player2.x, player1.y+50)

currentPlayer = player1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player1.x = player1.x -player1.increment
        player1.draw(screen)
    if pressed[pygame.K_RIGHT]:
        player1.x = player1.x + player1.increment
        player1.draw(screen)

    # fetch a sum for the current player
    sum = sumHelper.get_next_sum()

    # set the x/y based on sum answer


    # fill screen white
    screen.fill((255, 255, 255))

    # draw start and finish lines



    # divide between lines into x segments



    # draw players
    player1.draw(screen)
    player2.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    # has a player won?

    # toggle current player
    if currentPlayer == player1:
        currentPlayer = player2
    else:
        currentPlayer = player1
