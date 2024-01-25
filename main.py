from game_gui import GameGUI
from game import Game

if __name__ == '__main__':
    n = int(input('Enter the size of the board: '))
    c = int(input('Enter the number of cops: '))
    game = Game(n, c)
    game.run_game()

    #gui = GameGUI()
    #gui.run()