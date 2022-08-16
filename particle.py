import pygame
import numpy as np
import math

from settings import *
import random

def sigmoid(x):
    sig = np.where(x < 0, np.exp(x)/(1 / np.exp(x)), 1/(1 + np.exp(-x)))
    return sig

class Particle:
    def __init__(self, x:int, y:int, lifetime: int , behaviour: str, rect: pygame.rect.Rect, special: dict = {}) -> None:
        self.color = pygame.color.Color(144,122,24)
        self.keys = special.keys()
        if 'color' in self.keys:
            self.color = pygame.color.Color(special['color'])
        if 'alpha' in self.keys:
            self.color.a = special['alpha']
        self.screen = pygame.display.get_surface()
        self.x = x
        self.y = y
        self.lifetime = lifetime
        self.behaviour = behaviour
        self.entropy = 0
        self.rect = rect
        self.secondary_color = (255,0,0)

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class LightParticle(Particle):
    def __init__(self, x: int, y: int, lifetime: int, behaviour: str, special: dict = {}) -> None:
        self.radius = 20
        self.color = (14,14,14)
        self.surface = self.circle_surface()
        self.target = None
        if 'radius' in special.keys():
            self.radius = special['radius']
        if 'target' in special.keys():
            self.target = special['target']
        super().__init__(x, y, lifetime, behaviour, pygame.rect.Rect(0,0,0,0), special)



    def circle_surface(self):
        surf = pygame.Surface((self.radius * 2, self.radius * 2))
        pygame.draw.circle(surf, self.color, (self.radius, self.radius), self.radius)
        surf.set_colorkey((0,0,0))
        return surf

    def draw(self):
        # updating values
        #self.radius -= self.radius / self.radius + self.lifetime
        #self.surface = self.circle_surface()

        if self.target:
            self.screen.blit(self.surface, (self.target.rect.x + self.target.rect.width / 2- self.radius,
                                            self.target.rect.y + self.target.rect.height / 2 - self.radius),
                             special_flags=pygame.BLEND_RGB_ADD)
        else:
            self.screen.blit(self.surface, (self.x, self.y), special_flags=pygame.BLEND_RGB_ADD)

class ParticleHandler:
    def __init__(self) -> None:
        self.particles = []
        self.lights = []
        self.iter = 0
        self.spawn_interval = pygame.time.get_ticks()


    def update(self) -> None:
        for particle in self.particles:
            self.update_particle(particle)

    def draw(self) -> None:
        for particle in self.particles:
            particle.draw()

    def add_light(self, x, y, lifetime=100, behaviour='default', special={}):
        light = LightParticle(x, y, lifetime, behaviour, special)
        self.particles.append(light)


    def add_particle(self, x, y, width, height, lifetime, behaviour, special={}, interval=None):
        current_tick = pygame.time.get_ticks()
        rect = pygame.rect.Rect(x, y, width, height)
        if interval == None:
            particle = Particle(x, y, lifetime, behaviour, rect, special=special)
            self.particles.append(particle)

        else:
            if current_tick - self.spawn_interval > interval *1000:
                particle = Particle(x, y, lifetime, behaviour, rect, special=special)
                if 'light' in special.keys():
                    if 'light_mode' in special.keys():
                        if special['light_mode'] == 'follow':
                            special['target'] = particle
                            light = self.add_light(x, y, lifetime, behaviour, special)
                self.particles.append(particle)
                self.spawn_interval = current_tick
            else:
                pass


    def update_particle(self, particle):
        x = particle.rect.x
        y = particle.rect.y
        lifetime = particle.lifetime
        behaviour = particle.behaviour

        entropy = math.sin(self.iter)
        if particle.entropy == 0:
            particle.entropy = entropy
        self.iter += 1

        rngx = random.randint(2,5)
        rngy = random.randint(2,5)
        particle.lifetime -= 0.2
        if lifetime <= 0:
            self.particles.remove(particle)
        new_x = x - rngx
        new_y = y - rngy
        if behaviour == 'default':
            pass
        if behaviour == 'moving_up':
            new_x = x + particle.entropy
            new_y = y + rngy
        if behaviour == 'moving_down':
            new_x = x + particle.entropy
            new_y = y - rngy
        if behaviour == 'moving_left':
            new_x = x + rngx
            new_y = y + particle.entropy
        if behaviour == 'moving_right':
            new_x = x - rngx
            new_y = y + particle.entropy

        particle.rect.x = new_x
        particle.rect.y = new_y
