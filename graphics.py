import numpy as np
from path import map, Location, Cell
import pygame, sys


class guiWrapper:
    def __init__(self, randomMap: map):
        self.colCount = randomMap._columns
        self.rowCount = randomMap._rows
        self.grid = randomMap
        self.game = pygame.init()
        pygame.init()            
        self.screen = pygame.display.set_mode( (self.rowCount, self.colCount) )
        pygame.display.set_caption( 'A* search')
        self.arr = np.ndarray((self.rowCount, self.colCount, 3))
        # Empty: white, Blocked: black, Start: pink, Goal: blue, Path: red, Expand: light green, Generate, light red
        self.colors = np.array([[255, 255, 255], [0 , 0, 0], [255, 20, 147], [0, 0, 205], [255, 0, 0], [124, 252, 0], [205, 92, 92]])
    
    def setGrid(self):
        for row in range(self.rowCount):
            for col in range(self.colCount):
                if self.grid._grid[row][col] == Cell.EMPTY:
                    self.arr[row][col] = self.colors[0]
                if self.grid._grid[row][col] == Cell.BLOCKED:
                    self.arr[row][col] = self.colors[1]
                if self.grid._grid[row][col] == Cell.START:
                    self.arr[row][col] = self.colors[2]
                if self.grid._grid[row][col] == Cell.GOAL:
                    self.arr[row][col] = self.colors[3]
                if self.grid._grid[row][col] == Cell.PATH:
                    self.arr[row][col] = self.colors[4]
                if self.grid._grid[row][col] == Cell.EXPAND:
                    self.arr[row][col] = self.colors[5]
                if self.grid._grid[row][col] == Cell.GENERATE:
                    self.arr[row][col] = self.colors[6]


    def loop(self):
        surf = pygame.Surface((self.rowCount, self.colCount))
        pygame.surfarray.blit_array(surf, self.arr)
        surf = pygame.transform.scale(surf, (self.rowCount, self.colCount))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            self.screen.fill((0, 0, 0))
            self.screen.blit(surf, (0, 0))
            

#randomMap: map = map(500, 500, 0.15, Location(0, 0), Location(50 - 2, 50 - 2))
#wrap: guiWrapper = guiWrapper(randomMap)
#wrap.setGrid()
#wrap.loop()


