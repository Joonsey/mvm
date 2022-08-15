import pygame
from particle import ParticleHandler
from settings import *
import pygame.key

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, obstacles, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.image = pygame.image.load('test.png')
        if type(self.image) == None:
            raise ValueError('pepegae language server')
        self.rect = self.image.get_rect(topleft=(x,y))

        self.speed = 5
        self.obstacles = obstacles
        self.velocity = pygame.math.Vector2()
        self.particles = ParticleHandler()
        self.particle_spawn_interval = 0.1


    def handle_input(self):
        keys = pygame.key.get_pressed()

        if type(self.rect) == None:
            raise ValueError('please language server stop being mad')
            #"""have to typecheck because language server gets mad as rect 'might' be of type none"""

        if keys[pygame.K_w]:
            self.velocity.y = -1
            self.particles.add_particle(self.rect.centerx, self.rect.bottom, 1, 'moving_up', interval=self.particle_spawn_interval)
        elif keys[pygame.K_s]:
            self.velocity.y = 1
            self.particles.add_particle(self.rect.centerx, self.rect.y, 1, 'moving_down', interval=self.particle_spawn_interval)
        else:
            self.velocity.y = 0

        if keys[pygame.K_a]:
            self.velocity.x = -1
            self.particles.add_particle(self.rect.bottomright[0], self.rect.bottomright[1], 1, 'moving_left', interval=self.particle_spawn_interval)
        elif keys[pygame.K_d]:
            self.velocity.x = 1
            self.particles.add_particle(self.rect.bottomleft[0],self.rect.bottomleft[1], 1, 'moving_right', interval=self.particle_spawn_interval)
        else:
            self.velocity.x = 0

        if self.velocity.y and self.velocity.x:
            self.velocity = self.velocity.normalize()

        self.rect.x += self.velocity.x * self.speed

        self.rect.y += self.velocity.y * self.speed

    def update(self):
        self.handle_input()
        self.particles.update()
        self.particles.draw()

    def draw(self):
        print('does this even work')



