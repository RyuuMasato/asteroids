import sys
import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set static containers for game objects
    # After changing a static field like containers, make sure to create all objects after the change. This way, they will be correctly added to the groups.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Object initialization
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        # check for exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update group (player and others in group)
        for sprite in updatable:
            sprite: CircleShape
            sprite.update(dt)

        

        # check for asteroid collisions with player
        for asteroid in asteroids:
            asteroid: Asteroid
            
            # check for shot collisions with asteroids
            for shot in shots:
                shot: Shot
                # split or kill asteroid if shot colliding
                if asteroid.colliding(shot):
                    asteroid.split()

            # GAME OVER when player hit by asteroid
            if asteroid.colliding(player):
                print("Game over!")
                sys.exit()

        # draw black background
        black = pygame.Color(0, 0, 0, a=255)
        screen.fill(black)

        # draw group (player and others in group)
        for sprite in drawable:
            sprite: CircleShape
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
