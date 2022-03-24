from board import Board
from constants import *
#from random import rand


class Game:
    def __init__(self):
        self.game_board = Board()
        self.current_player = WHITE# if rand() > 0.5 else BLACK
        
        self.play()
            
    def play(self):
        running = True
        print(self.game_board)
        while running:
            move_list = self.get_movelist()
            self.win_by_block(move_list)
            selected_move = self.get_selected_move(move_list)
            self.game_board.move_piece(selected_move)
            self.game_board.promote_pieces()
            self.swap_turn()
            print(self.game_board)
            
    def get_movelist(self):
        print(f"{'White' if self.current_player == WHITE else 'Black'}'s turn, pick a move:\n") 
        move_list = self.game_board.get_moves(self.current_player)
        for num, move in enumerate(move_list):
            print(num+1, '. ', move, sep='')
        print()
        return move_list
        
    def get_selected_move(self, move_list):
        move = None
        try:
            move = input('Selected: ')
            move_index = int(move) - 1
            if move_index < 0 or move_index >= len(move_list):
                print("Invalid move index selected, try again.")
                return self.get_selected_move(move_list)
            return move_list[move_index]
        except:
            if move == 'ff' or move == 'FF':
                exit(0)
            print("Invalid move index selected, try again.")
            return self.get_selected_move(move_list)
               
    def swap_turn(self):
        self.current_player = WHITE if self.current_player == BLACK else BLACK
 
 
    def win_by_block(self, move_list):
        if len(move_list) == 0:
            print("Someone one, TODO figure this out later")