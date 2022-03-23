INITIAL_BOARD = [
        ['.', 'b', '.', 'b', '.', 'b', '.', 'b'],
        ['b', '.', 'b', '.', 'b', '.', 'b', '.'],
        ['.', 'b', '.', 'b', '.', 'b', '.', 'b'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['w', '.', 'w', '.', 'w', '.', 'w', '.'],
        ['.', 'w', '.', 'w', '.', 'w', '.', 'w'],
        ['w', '.', 'w', '.', 'w', '.', 'w', '.']]
        
BLACK_DELTAS = [(1,1), (-1,1)]
WHITE_DELTAS = [(-1,-1), (1,-1)]
KING_DELTAS = [(-1,-1), (1,-1), (1,1), (-1,1)]
WHITE = 'w'
BLACK = 'b'

def valid_coord(pair):
    x,y = pair
    return x > -1 and y > -1 and x < 8 and y < 8