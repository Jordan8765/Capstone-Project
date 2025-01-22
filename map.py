import pygame as pg

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, 1],
    [1, 3, 3, 3, 1, 3, 3, 4, 1, 3, 3, _, _, 3, 3, 2],
    [1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 7, _, _, 7, 10, 2],
    [1, 2, 5, 5, 5, 2, 2, 2, 2, 2, 9, _, _, 9, _, 2],
    [5, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 6],
    [9, _, _, _, _, _, _, _, _, _, 2, 2, 2, _, _, 6],
    [9, _, _, 5, 5, 5, 5, _, _, _, _, _, 2, _, _, 6],
    [9, _, _, 5, _, _, _, _, _, _, _, _, 2, _, _, 6],
    [7, _, _, 5, _, _, _, _, _, _, _, _, _, _, _, 6],
    [9, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 6],
    [5, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 6],
    [1, 6, 6, 6, 8, 8, _, _, _, _, _, 8, 8, 6, 6, 1],
    [1, 1, 14, 15, 8, 8, _, _, _, _, _, 8, 8, 6, 6, 1],
    [1, _, _, _, 8, 8, _, _, _, _, _, 8, 8, 11, 12, 1],
    [4, _, _, _, 4, 4, _, _, _, _, _, 8, 4, _, _, 4],
    [4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [4, _, _, _, _, _, _, _, _, _, 1, 1, 1, _, _, 4],
    [4, _, _, 1, _, _, _, _, _, _, 1, _, 1, _, _, 4],
    [4, _, _, 1, _, _, _, _, _, _, _, _, 1, _, _, 4],
    [4, _, _, 1, _, _, _, _, _, _, 1, 1, 1, _, _, 4],
    [4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
