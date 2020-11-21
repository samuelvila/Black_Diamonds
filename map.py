import pygame

import var


class Map:
    def __init__(self):
        self.tile_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 6, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 1, 5, 0, 0, 0, 0, 5, 2, 2, 2, 2, 6, 0, 0, 4],
                         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.tile_set = [
            pygame.image.load("res/img/map1/mid.png"),
            pygame.image.load("res/img/map1/top.png"),
            pygame.image.load("res/img/map1/left_wall.png"),
            pygame.image.load("res/img/map1/left_corner.png"),
            pygame.image.load("res/img/map1/right_wall.png"),
            pygame.image.load("res/img/map1/right_corner.png")]
        self.tile_hit = []

    def render(self, frame):
        self.tile_hit = []
        y = 8
        for row in self.tile_map:
            x = 0
            for column in row:
                if column != 0:
                    frame.blit(self.tile_set[column-1], (x*var.TILE_SIZE, y*var.TILE_SIZE))
                    self.tile_hit.append(pygame.Rect(x*var.TILE_SIZE, y*var.TILE_SIZE, var.TILE_SIZE, var.TILE_SIZE))
                x += 1
            y += 1
