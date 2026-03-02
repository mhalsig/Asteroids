import pygame

from logger import log_state
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids with pygame version:", pygame.version.vernum)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    dt = 0
    clock = pygame.time.Clock()

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

  

if __name__ == "__main__":
    main()
