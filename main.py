import sys
import pygame

from shot import Shot
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids with pygame version:", pygame.version.vernum)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    dt = 0
    clock = pygame.time.Clock()

    shots = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroidField = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

  

if __name__ == "__main__":
    main()
