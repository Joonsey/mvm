import pygame
import sys
from level import Level
from settings import HEIGHT, WIDTH


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.level = Level()


    def run(self)->None:
        while True:
            pygame.time.Clock().tick(60)
            self.screen.fill((0,0,0,0))
            self.level.visible_group.update()
            self.level.visible_group.draw(self.screen)
            pygame.display.update()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if keys[pygame.K_q]:
                pass
                #self.level.player.rect.x += 20



if __name__ == "__main__":
    game = Game()
    game.run()
