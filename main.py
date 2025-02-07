import pygame
from src import pianoplayer as player
from src import constants as c 

def main():

    print("Starting the piano!")
    
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()

    player.PianoPlayer.containers = (updatable)

    piano_player = player.PianoPlayer()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color("#273136"))
        
        for obj in updatable:
            obj.update()
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    main()
