class Player:
    def __init__(self, board):
        self.board = board
        self.x = None
        self.y = None

    
    def move(self):
        pass

class Robber(Player):
    def __init__(self, board):
        super().__init__(board)
    
    def handle_user_input(self):
        valid_inputs = ['w', 'a', 's', 'd']
        # Get user input and validate it
        while True:
            direction = input('Enter a direction (w, a, s, d): ').lower()
            if direction in valid_inputs:
                break
            else:
                print('Invalid direction. Try again.')
        return direction

    def move(self):
        # Update the robber's position on the board and check if the robber hits the board's boundary
        while True:
            direction = self.handle_user_input()
            if direction == 'w':
                if self.x == 0:
                    print('You hit a boundary. Try again.')
                else:
                    self.x -= 1
                    break
            elif direction == 'a':
                if self.y == 0:
                    print('You hit a boundary. Try again.')
                else:
                    self.y -= 1
                    break
            elif direction == 's':
                if self.x == self.board.size - 1:
                    print('You hit a boundary. Try again.')
                else:
                    self.x += 1
                    break
            elif direction == 'd':
                if self.y == self.board.size - 1:
                    print('You hit a boundary. Try again.')
                else:
                    self.y += 1
                    break
        self.board.grid[self.x][self.y] = 'R'
        self.board.display()

        
        
    

class Cop(Player):
    def __init__(self, board):
        super().__init__(board)

    def move(self):
        # TODO: Implement the cop's movement
        pass