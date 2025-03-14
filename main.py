# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

clock = pygame.time.Clock()
dt = 0

def main():

    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                    
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()