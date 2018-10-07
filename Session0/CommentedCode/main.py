#---------------------------------------------------------------------------

from GameOfLife import *         # imports all the functions inside GameOfLife.py
from GameParameters import *     # imports the parameters to be used here

# thisGen[] & nextGen[] are Python lists that acts as 2D matrices that holds the data whether a cell is alive or dead.
# thisGen[] holds the data for the current generation.
# nextGen[] holds the data for the next generation as it purely depends on the previous condition i.e thisGen[] here.

thisGen = []
nextGen = []

# initGrid() is a function included in library GameOfLife.py which gives 
# the list (which is passed), an initial state which is completely random.

initGrid(ROWS, COLS,  thisGen)

# printGen() is a function included in library GameOfLife.py which prints 
# the generation (2D matrix).

# processNextGen() generates the next generation (next 2D matrix) which is 
# totaly dependent upon the previous generation (current generation 2D matrix),
# and hence both (thisGen[] and nextGen[]) are arguments to this function.

# sleep() is a function in the library "time" which takes arguments in seconds.
# It produces delay between the previous generation and the next generation.

nextGen = copy.deepcopy(thisGen)

printGen(ROWS, COLS, thisGen, 0)

for gens in range(GENERATIONS):
    processNextGen(ROWS, COLS, thisGen, nextGen)
    printGen(ROWS, COLS, nextGen, gens)
    input()

# Once current generation is done printing. The next generation is now 
# proceessed the next generation to be printed out next.
# At last thisGen has been assigned the value of nextGen for getting copied.

    thisGen = copy.deepcopy(nextGen)

input("Finished. Press <return> to quit.")
