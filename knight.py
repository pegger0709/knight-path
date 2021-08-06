import random
import numpy as np
import matplotlib.pyplot as plt
from chessboard import Chessboard

class Knight:
    def __init__(self, chessboard=None, square=-1):
        self.chessboard = Chessboard() if chessboard is None else chessboard
        if square == -1:
            self.square = random.randint(0, self.chessboard.nrank * self.chessboard.nfile - 1)
            print('initializing at random square %d' % self.square)
        elif not (0 <= square < self.chessboard.nrank * self.chessboard.nfile - 1):
            self.square = random.randint(0, self.chessboard.nrank * self.chessboard.nfile - 1)
            print('%d is not a legal square on the chessboard; initializing at random square %d' % (square, self.square))
        else:
            self.square = square
        self.visited_squares = [self.square]
    def getPossibleMoves(self, *, visited=False):
        i = self.square % self.chessboard.nfile
        j = self.square // self.chessboard.nrank
        legal_moves = []
        for move in [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]:
            if 0 <= i+move[0] < self.chessboard.nfile and 0 <= j+move[1] < self.chessboard.nrank:
                destination = (j+move[1])*self.chessboard.nfile + (i+move[0])
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
    def randomWalk(self):
        while self.getPossibleMoves(visited=False):
            self.move(random.choice(self.getPossibleMoves(visited=False)))
    def pivotPath(self, pivot):
        if pivot not in self.getPossibleMoves(visited=True):
            print('%d is not a valid pivot')
        else:
            new_path = []
            i = 0
            old_path = self.visited_squares
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
        pivot = random.choice(list(set(self.getPossibleMoves(visited=True)).difference({self.visited_squares[-2]})))
        self.pivotPath(pivot)
        self.randomWalk()
    def traverseChessboard(self):
        self.randomWalk()
        while len(self.visited_squares) < self.chessboard.nrank * self.chessboard.nfile:
            self.unblock()
    def plotTraversal(self):
        self.chessboard.plot()
        for i in range(len(self.visited_squares) - 1):
            tail = self.visited_squares[i]
            head = self.visited_squares[i+1]
            x_tail = tail % self.chessboard.nfile
            y_tail = tail // self.chessboard.nrank
            x_head = head % self.chessboard.nfile
            y_head = head // self.chessboard.nrank
            plt.arrow(x_tail, y_tail, x_head-x_tail, y_head-y_tail, head_width=0.1, color='red')
        plt.show()


