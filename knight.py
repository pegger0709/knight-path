import random
class Knight:
    def __init__(self, square=-1):
        if square == -1:
            self.square = random.randint(0,63)
            print('initializing at random square %d' % self.square)
        elif not (0 <= square < 63):
            self.square = random.randint(0,63)
            print('%d is not a legal square on the chessboard; initializing at random square %d' % (square, self.square))
        else:
            self.square = square
        self.visited_squares = [self.square]


