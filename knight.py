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

    def getPossibleMoves(self, *, visited=False):
        i = self.square % 8
        j = self.square // 8
        legal_moves = []
        for move in [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]:
            if 0 <= i+move[0] < 8 and 0 <= j+move[1] < 8:
                destination = (j+move[1])*8 + (i+move[0])
                if not visited and (destination not in self.visited_squares):
                    legal_moves.append(destination)
                elif visited and (destination in self.visited_squares):
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
        while self.getPossibleMoves(visited=False):
            self.move(random.choice(self.getPossibleMoves(visited=False)))

    def pivotPath(self, pivot):
        if pivot not in self.getPossibleMoves(visited=True):
            print('%d is not a valid pivot')
        else:
            new_path = []
            i = 0
            old_path = k.visited_squares
            while old_path[i] != pivot:
                new_path.append(old_path[i])
                i += 1
            new_path.append(pivot)
            i = -1
            while old_path[i] != pivot:
                new_path.append(old_path[i])
                i -= 1
            self.visited_squares = new_path
            self.square = new_path[-1]

    def unblock(self):
        pivot = random.choice(self.getPossibleMoves(visited=True))
        self.pivotPath(pivot)
        self.startRandomWalk()

    def traverseChessboard(self):
        self.startRandomWalk()
        while len(self.visited_squares) < 64:
            self.unblock()
