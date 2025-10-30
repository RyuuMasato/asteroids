import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        color = pygame.Color(255, 255, 255, a=255)
        pygame.draw.circle(surface=screen, color=color, center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)