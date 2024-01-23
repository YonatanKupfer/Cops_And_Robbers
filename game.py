import tkinter as tk
from board import Board
from player import Robber, Cop

class Game:
    def __init__(self, n, c):
        self.board = Board(n)
        self.robber = Robber(self.board)
        self.cops = [Cop(self.board) for i in range(c)]
        self.board.place_cops(self.cops)

        self.board.display()

    def play_turn(self):
        self.robber.move()
        for cop in self.cops:
            cop.move()

    def is_game_over(self):
        # TODO: Implement the game over logic
        pass