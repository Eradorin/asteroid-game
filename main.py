# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
#import time

def main():

    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
   # time.sleep(0.5)

    while True:
        for event in pygame.event.get():
            #print(f"Event: {event.type}")
            if event.type == pygame.QUIT:
               # print("Quit event detected")
                return
            
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()