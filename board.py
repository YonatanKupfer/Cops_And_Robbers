import random

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = self.generate_grid()

    def generate_grid(self):
        grid = [[' ' for i in range(self.size)] for j in range(self.size)]
        return grid
    
    def display(self):
        for row in self.grid:
            print(' '.join(row))

    def place_cops(self, cops):
      for cop in cops:
        x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        while self.grid[x][y] != ' ':
          x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        self.grid[x][y] = 'C'
        cop.x, cop.y = x, y

        