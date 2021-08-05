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

    def getPossibleMoves(self):
        i = self.square % 8
        j = self.square // 8
        legal_moves = []
        for move in [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]:
            if 0 <= i+move[0] < 8 and 0 <= j+move[1] < 8:
                destination = (j+move[1])*8 + (i+move[0])
                if destination not in self.visited_squares:
                    legal_moves.append(destination)
        return legal_moves

    def move(self, destination):
        if destination not in self.getPossibleMoves():
            print('Knight cannot reach square %d from square %d' % (destination, self.square))
            pass
        else:
            self.square = destination
            self.visited_squares.append(destination)

    def startRandomWalk(self):
        while self.getPossibleMoves():
            self.move(random.choice(self.getPossibleMoves()))

