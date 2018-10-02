#---------------------------------------------------------------------------

from GameOfLife import *
from GameParameters import *

thisGen = []
nextGen = []

initGrid(COLS, ROWS, thisGen)
initGrid(COLS, ROWS, nextGen)

for gens in range(GENERATIONS):
    printGen(COLS, ROWS, thisGen, gens)
    processNextGen(COLS, ROWS, thisGen, nextGen)
    time.sleep(DELAY)
    thisGen, nextGen = nextGen, thisGen
input("Finished. Press <return> to quit.")
