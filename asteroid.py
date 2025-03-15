import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        self.containers = Asteroid.containers
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        print(f"Splitting asteroid with radius: {self.radius}")
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            new_velocity1 = self.velocity.rotate(random_angle) * 1.2
            new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            print(f"New radius: {new_radius}")
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid1.velocity = new_velocity1
            new_asteroid2.velocity = new_velocity2
