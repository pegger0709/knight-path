import numpy as np
import matplotlib.pyplot as plt
import string

class Chessboard:
    def __init__(self, nrank=8, nfile=8):
        self.nrank = nrank
        self.nfile = nfile
    def plot(self):
        chessboard = np.array([[(i+j)%2 for i in range(self.nfile)] for j in range(self.nrank)])
        plt.imshow(chessboard, cmap='gray')
        plt.xticks(range(self.nfile),list(string.ascii_uppercase[:self.nfile]))
        plt.yticks(range(self.nrank),range(self.nrank,1-1,-1))

