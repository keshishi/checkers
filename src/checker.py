class Checker:
    def __init__(self, x, y, c, board):
        self.king = False
        self.x = x
        self.y = y
        self.color = c
        self.board = board

    def __str__(self):
        return self.color
    
    def is_color(self, color):
		return self.color == color
		
    
    def get_moves(self):
        print(self.board[0,0])
        return 