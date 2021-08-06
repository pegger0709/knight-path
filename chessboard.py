import numpy as np
import matplotlib.pyplot as plt
import string

class Chessboard:
    def __init__(self, nrank=8, nfile=8):
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
    def plot(self):
        chessboard = np.array([[(i+j)%2 for i in range(self.nfile)] for j in range(self.nrank)])
        plt.imshow(chessboard, cmap='gray')
        plt.xticks(range(self.nfile),list(string.ascii_uppercase[:self.nfile]))
        plt.yticks(range(self.nrank),range(self.nrank,1-1,-1))

