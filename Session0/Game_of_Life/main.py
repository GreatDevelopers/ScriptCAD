#---------------------------------------------------------------------------

from GameOfLife import *
from GameParameters import *

thisGen = []
nextGen = []

initGrid(ROWS, COLS,  thisGen)

nextGen = copy.deepcopy(thisGen)

printGen(ROWS, COLS, thisGen, 0)

for gens in range(1, GENERATIONS):
    processNextGen(ROWS, COLS, thisGen, nextGen)
    printGen(ROWS, COLS, nextGen, gens)
    input()
    thisGen = copy.deepcopy(nextGen)
input("Finished. Press <return> to quit.")
