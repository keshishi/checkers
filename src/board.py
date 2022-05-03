class Board:
    def __init__(self):
        
        self.board = self.create_board()
        self.turn = 0
        self.print_board()
        self.get_moves()
           
    
    def create_board(self):
        board = list()
        for i in range(8):
            board.append(list())
            for j in range(8):
                board[i].append(0)
        
        for i in range(3):
            for j in range(len(board[i])):
                if (i+j) % 2 == 1:
                    board[i][j] = 0b001
                    
        for i in range(5,8):
            for j in range(len(board[i])):
                if (i+j) % 2 == 1:
                    board[i][j] = 0b011
        return board
        
    
    def print_board(self):
        def convert_to_piece(val):
            # We are able to represent pieces on the board with the first 3 bits of a number 
            # first bit represennt the presence of a piece, second bit represents its color, 
            # third bit represents whether or not its a king yet
            piece = '.'
            if val & 0b001: # Non-empty
                if val & 0b010: # white
                    piece = 'w'
                else:       # black
                    piece = 'b'
                if val & 0b100: # KING
                    piece = piece.upper()
            return piece
        
        output = '  A B C D E F G H'
        for row in range(len(self.board)):
            output += f'\n{8-row}'
            for col in self.board[row]:
                output += f' {convert_to_piece(col)}'
        print(output)
        
    def get_moves(self):
        if self.turn % 2:
            print("black move")
        else:
            for row in range(len(self.board):
                for col in range(len(self.board[row])):
                    if self.board[row][col] & 0b011:
                        pass
            print("white move")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        