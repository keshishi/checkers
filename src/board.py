from checker import Checker
from constants import INITIAL_BOARD


class Board:
    def __init__(self) -> None:
        self.board = self.__create_board()
        print(self)

    def __str__(self):
        out = ""
        for checker in self:
            out += str(checker) + ' '
        return out

    def __iter__(self):
        self.x = 0
        self.y = 0
        return self

    def __next__(self):
        if self.x >= 7:
            self.x = 0
            self.y += 1
        if self.y > 7:
            raise StopIteration
        self.x += 1
        return self.board[self.y][self.x]


    def __create_board(self) -> list[list[Checker]]:
        board = list()
        for y, r in enumerate(INITIAL_BOARD):
            row = list()
            for x, char in enumerate(r):
                row.append(Checker(x, y, char))
            board.append(row)
        return board

    def get_moves(self, color):

        pass
