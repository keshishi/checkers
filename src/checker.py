from constants import *
from collections import defaultdict

class Move:
    def __init__(self, start, end, kill):
        self.start_pos = start
        self.end_pos = end
        self.kill = kill
        
    def __str__(self):
        return repr(self.start_pos) + '->' + repr(self.end_pos)
        
    def __repr__(self):
        return repr(self.start_pos) + '->' + repr(self.end_pos)
        
class Checker:
    def __init__(self, x, y, c, board):
        self.king = False
        self.x = x
        self.y = y
        self.color = c
        self.board = board

    def __str__(self):
        return self.color.upper() if self.king else self.color
    
    def is_color(self, color):
        return self.color == color
        
    def is_not_ally(self, coord):
        return self.color != self.board[coord].color
        
    def get_moves(self):
        moves = defaultdict(list)
        delta_set = KING_DELTAS if self.king else (WHITE_DELTAS if self.is_color(WHITE) else BLACK_DELTAS)
        for x_delta, y_delta in KING_DELTAS:
            potential_coord = (self.x + x_delta, self.y + y_delta)
            if valid_coord(potential_coord):
                if self.board.is_unoccupied(potential_coord):
                    moves['general'].append(Move((self.x, self.y), potential_coord, False))
                elif self.is_not_ally(potential_coord):
                    potential_coord = (self.x + x_delta*2, self.y + y_delta*2)
                    if valid_coord(potential_coord) and self.board.is_unoccupied(potential_coord) :
                        moves['forced'].append(Move((self.x, self.y), potential_coord, True))    
        return moves
        
    def copy_color(self, piece):
        self.color = piece.color
        self.king = piece.king
        
    def clear_piece(self):
        self.color = '.'
        self.king = False