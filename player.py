import pygame
from particle import ParticleHandler
from settings import *
import pygame.key

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, obstacles, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.image = pygame.image.load('character-0.png')
        self.rect = self.image.get_rect(topleft=(x,y))

        self.speed = 5
        self.obstacles = obstacles
        self.velocity = pygame.math.Vector2()
        self.particles = ParticleHandler()
        self.particle_spawn_interval = 0.1
        self.particle_lifetime = 5

        self.dash_distance = self.speed * 6
        self.is_dashing = False
        self.dash_interval = 600
        self.last_dash = 0

        self.direction = self.velocity


    def handle_input(self):
        keys = pygame.key.get_pressed()

        if type(self.rect) == None:
            raise ValueError('please language server stop being mad')
            #"""have to typecheck because language server gets mad as rect 'might' be of type none"""


        if keys[pygame.K_a]:
            self.velocity.x = -1
            self.image = pygame.image.load('character-1.png')
            self.particles.add_particle(self.rect.bottomright[0],
                                        self.rect.bottomright[1],
                                        2,2,
                                        self.particle_lifetime,
                                        'moving_left',
                                        interval=self.particle_spawn_interval,
                                        special={'light': True, 'light_mode': 'follow'})
        elif keys[pygame.K_d]:
            self.velocity.x = 1
            self.image = pygame.image.load('character-2.png')
            self.particles.add_particle(self.rect.bottomleft[0],
                                        self.rect.bottomleft[1],
                                        2,2,
                                        self.particle_lifetime,
                                        'moving_right',
                                        interval=self.particle_spawn_interval,
                                        special={'light': True, 'light_mode': 'follow'})
        else:
            self.velocity.x = 0

        if keys[pygame.K_w]:
            self.velocity.y = -1
            self.image = pygame.image.load('character-3.png')
            self.particles.add_particle(self.rect.centerx,
                                        self.rect.bottom,
                                        2,2,
                                        self.particle_lifetime ,
                                        'moving_up',
                                        interval=self.particle_spawn_interval,
                                        special={'light': True, 'light_mode': 'follow'})
        elif keys[pygame.K_s]:
            self.velocity.y = 1
            self.image = pygame.image.load('character-0.png')
            self.particles.add_particle(self.rect.centerx,
                                        self.rect.y,
                                        2,2,
                                        self.particle_lifetime,
                                        'moving_down',
                                        interval=self.particle_spawn_interval,
                                        special={'light': True, 'light_mode': 'follow'})
        else:
            self.velocity.y = 0

        self.direction = self.velocity.copy()
        if self.direction.x == 0 and self.direction.y == 0:
            self.direction.x = 1

        if self.velocity.y and self.velocity.x:
            self.velocity = self.velocity.normalize()

        if keys[pygame.K_SPACE]:
            ct = pygame.time.get_ticks()
            dt = ct - self.last_dash
            if dt > self.dash_interval:
                self.is_dashing = False
                if self.is_dashing:
                    pass
                else:
                    self.rect.x += self.velocity.x * self.dash_distance
                    self.rect.y += self.velocity.y * self.dash_distance
                    self.is_dashing = True
                    self.last_dash = pygame.time.get_ticks()

        self.rect.x += self.velocity.x * self.speed

        self.rect.y += self.velocity.y * self.speed


    def update(self):
        self.handle_input()
        self.particles.update()
        self.particles.draw()

    def draw(self):
        print('does this even work')



