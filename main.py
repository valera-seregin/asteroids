import sys
import pygame
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()

    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for drw in drawable:
            drw.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

