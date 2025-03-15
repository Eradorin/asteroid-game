import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

clock = pygame.time.Clock()
dt = 0

def main():

    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots_group)
    asteroidfield = AsteroidField()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS, shots_group)

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                    
        updateable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                import sys
                sys.exit()
        for shot in shots_group:
            shot.update(dt)

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)
        for shot in shots_group:
            shot.draw(screen)
        #drawable.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()