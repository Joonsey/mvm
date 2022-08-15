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
        self.surface = pygame.display.get_surface()
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
        pygame.draw.rect(self.surface, self.color, self.rect)

class ParticleHandler:
    def __init__(self) -> None:
        self.particles = []
        self.iter = 0
        self.spawn_interval = pygame.time.get_ticks()


    def update(self) -> None:
        for particle in self.particles:
            self.update_particle(particle)

    def draw(self) -> None:
        for particle in self.particles:
            particle.draw()

    def add_particle(self, x, y, lifetime, behaviour, special=None, interval=None):
        current_tick = pygame.time.get_ticks()
        rect = pygame.rect.Rect(x, y, 8, 8)
        if interval == None:
            particle = Particle(x, y, lifetime, behaviour, rect)
            self.particles.append(particle)
        else:
            if current_tick - self.spawn_interval > interval *1000:
                particle = Particle(x, y, lifetime, behaviour, rect)
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
