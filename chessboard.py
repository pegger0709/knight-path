import numpy as np
import matplotlib.pyplot as plt
import string

class Chessboard:
    """
    class Chessboard represents a rectangular chessboard for the knight to travel on

    Attributes
    ----------
    nrank: int
        the rank of the chessboard, i.e. the number of rows (default 8)
    nfile: int
        the file of the chessboard, i.e. the number of columns (default 8)

    Methods
    -------
    plot()
        prepares a matplotlib plot of the chessboard, in order to visualize the knight's tour
    """
    def __init__(self, nrank=8, nfile=8):
        """
        Parameters
        ----------
        nrank: int
            the rank of the chessboard, i.e. the number of rows (default 8)
        nfile: int
            the file of the chessboard, i.e. the number of columns (default 8)

        Constraints
        -----------
        In 1991, A.J. Schwenk proved that any m * n chessboard with m <= n
        admits a closed knight's tour unless one of the three following conditions hold:
            1. m and n are both odd
            2. m = 1, 2, or 4
            3. m = 3 and n = 4, 6, or 8
        """
        self.nrank = nrank
        self.nfile = nfile
        m = min([nrank, nfile])
        n = max([nrank, nfile])
        if m%2==1 and n%2==1:
            print('m=%d and n=%d are both odd, a closed tour may not be possible' % (m,n))
        elif m==1 or m==2 or m==4:
            print('m=%d: for m=1, 2, or 4, a closed tour may not be possible' % m)
        elif m==3 and (n==4 or n==6 or n==8):
            print('m=%d, n=%d: for m=3 and n=4, 6, or 8, a closed tour may not be possible' % (m,n))
        else:
            print('A closed tour is possible')

    def plot(self, show=False):
        """
        Parameters
        ----------
        show: bool
            If True, then display the plot of the blank chessboard.
            If False, then create the plot but do not display,
            in order to draw arrows representing knight's tour (default)
        """
        chessboard = np.array([[(i+j)%2 for i in range(self.nfile)] for j in range(self.nrank)])
        plt.imshow(chessboard, cmap='gray')
        plt.xticks(range(self.nfile),list(string.ascii_uppercase[:self.nfile]))
        plt.yticks(range(self.nrank),range(self.nrank,1-1,-1))
        if show:
            plt.show()
