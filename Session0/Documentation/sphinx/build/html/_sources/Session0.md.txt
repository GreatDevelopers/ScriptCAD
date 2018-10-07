# A date with Python!

## Introduction:

### 1. What is Game Of Life?

The Game of Life, also known simply as Life, has been devised by the British mathematician `John Horton Conway` in 1970.

The game is a `zero-player` game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced players, by creating patterns with particular properties. 

##### Rules:

The universe of the Game of Life is an infinite, `two-dimensional` orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.

![Square](images/Square.png)

**At each step in time, the following transitions occur:**

	1. Any live cell with fewer than two live neighbors dies, as if by under population.
	2. Any live cell with two or three live neighbors lives on to the next generation.
	3. Any live cell with more than three live neighbors dies, as if by overpopulation.
	4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously. The rules continue to be applied repeatedly to create further generations. 


