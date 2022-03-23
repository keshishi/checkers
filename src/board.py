from checker import Checker, Move
from constants import INITIAL_BOARD


class Board:
    def __init__(self) -> None:
        self.board = self.__create_board()

    def __str__(self) -> str:
        out = "\n  0 1 2 3 4 5 6 7\n"
        for row_num, row in enumerate(self.board):
            out += str(row_num) + ' '
            for checker in row:
                out += str(checker) + ' '
            out += '\n'
        return out

    def __iter__(self):
        self.x = 0
        self.y = 0
        return self

    def __next__(self) -> Checker:
        if self.y > 7:
            raise StopIteration
        piece = self[self.x, self.y]
        self.x += 1
        if self.x > 7:
            self.x = 0
            self.y += 1
        return piece

    def __getitem__(self, key) -> Checker:
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
                options = checker.get_moves()
                force_moves.extend(options['forced'])
                moves.extend(options['general'])
        return force_moves if len(force_moves) > 0 else moves
        
    def is_unoccupied(self, pair) -> bool:
        return self[pair].is_color('.')
        
    def move_piece(self, move):
        if move.kill:
            pass
        else:
            self[move.end_pos].copy_color(self[move.start_pos])
            self[move.start_pos].clear_piece()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
