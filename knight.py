import random
import numpy as np
import matplotlib.pyplot as plt
from chessboard import Chessboard

class Knight:
    """
    class Knight represents the knight that will perform a closed tour
    on a given rectangular chessboard, visiting each square exactly once
    in such a way that the end of the tour is a knight's move away from the start.

    Attributes
    ----------
    chessboard: Chessboard object
        The board on which the knight is to find a closed tour.
    square: int
        The square on which the knight currently stands
    visited_squares: list of int
        The list of all squares the knight has visited so far in its tour

    Methods
    -------
    getPossibleMoves(visited=False)
        Returns list of previously unvisited (or visited) squares accessible
        in one knight's move from the current square
    move(destination)
        Moves the knight to the destination square
    randomWalk()
        Sends the knight on a random walk across unvisited squares
    pivotPath(pivot)
        Pivots the walk of the knight (todo: write better description)
    unblock()
        When the knight is stuck, continue pivoting until the knight becomes unstuck
    traverseChessboard()
        Perform a closed tour
    plotTraversal():
        Create a matplotlib plot depicting the knight's path thus far
    """
    def __init__(self, chessboard=None, square=-1):
        """
        Parameters
        ----------
        chessboard: Chessboard object
            The board on which the knight is to find a closed tour. (default 8*8)
            The squares are labeled from 0 to rank * file - 1
            starting at the upper left corner and traveling first along the top row.
        square: int
            The square on which the knight's tour begins. If -1, then a random initial square is chosen (default -1)
        visited_squares: list of int
            The list of all squares the knight has visited so far in its tour.
        """
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

    def __repr__(self):
        repr = 'knight is located at square %d' % self.square
        repr += '\n'
        repr += 'knight has visited squares ' + str(self.visited_squares)
        repr += '\n'
        repr += 'knight has not visited squares ' + str(list(set(range(self.chessboard.nrank * self.chessboard.nfile)).difference(set(self.visited_squares))))
        return repr

    def getPossibleMoves(self, *, visited=False):
        """
        Finds all squares accessible to the knight from the current square by one knight's move

        Parameters
        ----------
        visited: bool
            If True, return the list of accessible squares which have already been visited
            If False, return the list of accessible squares which have not already been visited

        Returns
        -------
        list(int)
            A list of integers corresponding to those visited (or unvisited)
            squares reachable from the current square by a knight's move.
            We want the unvisited squares if we're pursuing a tour, and we want
            the visited squares if we're looking for a square to pivot on.

        """
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
        """
        Moves the knight to the given square, provided this is possible with one knight's move

        Parameters
        ----------
        destination: int
            The square to which we want to move the knight
        """
        if destination not in self.getPossibleMoves():
            print('Knight cannot reach square %d from square %d' % (destination, self.square))
            pass
        else:
            self.square = destination
            self.visited_squares.append(destination)

    def randomWalk(self):
        """
        Sends the knight on a random walk as long as it can move on unvisited squares
        """
        while self.getPossibleMoves(visited=False):
            self.move(random.choice(self.getPossibleMoves(visited=False)))

    def pivotPath(self, pivot):
        """
        Pivots the knight's tour on a given square (todo: write better description)

        Parameters
        ----------
        pivot: int
            The square to pivot on
        """
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
        """
        When the knight is stuck, continue attempting to pivot until it can continue the tour
        """
        pivot = random.choice(list(set(self.getPossibleMoves(visited=True)).difference({self.visited_squares[-2]})))
        self.pivotPath(pivot)
        self.randomWalk()

    def traverseChessboard(self):
        """
        Sends the knight on a complete knight's tour of the chessboard
        """
        self.randomWalk()
        while len(self.visited_squares) < self.chessboard.nrank * self.chessboard.nfile:
            self.unblock()

    def plotTraversal(self):
        """
        Produces a matplotlib figure depicting the knight's tour on the chessboard
        """
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
