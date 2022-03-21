from checker import Checker
from constants import INITIAL_BOARD


class Board:
    def __init__(self) -> None:
        self.board = self.__create_board()
        print(self)

    def __str__(self):
        out = ""
        for row in self.board:
            for checker in row:
                out += str(checker) + ' '
            out += '\n'
        return out

    def __iter__(self):
        self.x = 0
        self.y = 0
        return self

    def __next__(self):
        piece = self[self.x, self.y]
        self.x += 1
        if self.x > 7:
            self.x = 0
            self.y += 1
        if self.y > 7:
            raise StopIteration
        return piece

    def __getitem__(self, key):
        return self.board[key[1]][key[0]]

    def __create_board(self) -> list[list[Checker]]:
        board = list()
        for y, r in enumerate(INITIAL_BOARD):
            row = list()
            for x, char in enumerate(r):
                row.append(Checker(x, y, char, self))
            board.append(row)
        return board

    def get_moves(self, color):
		force_moves = list()
		moves = list()
        for checker in self:
            if checker.is_color(color):
                options = checker.get_moves(self)
                force_moves.extend(options['eat'])
                moves.extend(options['move'])
        return force_moves if len(force_moves) > 0 else moves
                