import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, variation, x, y, *groups: pygame.sprite.AbstractGroup, special: dict = {}) -> None:
        super().__init__(*groups)
        rect_x = x
        rect_y = y
        width = tile_size
        height = tile_size
        special_dict = special.keys()
        if ['x_offset'] in special_dict:
            rect_x += special['x_offset']
        if ['y_offset'] in special_dict:
            rect_y += special['y_offset']
        if ['width_offset'] in special_dict:
            width += special['width_offset']
        if ['height_offset'] in special_dict:
            height += special['height_offset']
        self.rect = pygame.rect.Rect(rect_x,rect_y,tile_size, tile_size)


    def draw(self):
        pass

