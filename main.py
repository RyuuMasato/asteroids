# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # After changing a static field like containers, make sure to create all Player objects after the change. This way, they will be correctly added to the groups.
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        # check for exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update group (player and others in group)
        for sprite in updatable:
            sprite.update(dt)

        # draw black background
        black = pygame.Color(0, 0, 0, a=255)
        screen.fill(black)

        # draw group (player and others in group)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
