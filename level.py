from typing import List
import pygame
from particle import ParticleHandler
from player import Player
from tile import Tile
from settings import *

class Level:
    def __init__(self) -> None:
        self.index = 0
        self.collision_group = pygame.sprite.Group()
        self.visible_group = pygame.sprite.Group()
        self.parsed_map = self.parse_map()
        self.make_tiles()
        self.particles = ParticleHandler()

    def make_tiles(self) -> None:
        for y, _ in enumerate(self.parsed_map):
            for x, value in enumerate(self.parsed_map[y]):
                xpos = x* tile_size
                ypos = y*tile_size
                if int(value) == 1:
                    #tile = Tile(x * tile_size, y * tile_size, self.visible_group)
                    self.player = Player(xpos, ypos, self.collision_group, self.visible_group)

    def parse_map(self, optional_path = 'map') -> List[List[int]]:
        data = []
        with open(optional_path, 'r') as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                data.append(line.split(','))
        return data

    def draw(self):
        pass
    def update(self):
        pass
