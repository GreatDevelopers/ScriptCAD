---
Title : Session-0
---

<link rel = "stylesheet" href = "style/intro.css">
 
<link rel = "stylesheet" href = "https://www.w3schools.com/w3css/4/w3.css">

<div class="w3-bar w3-light-grey">
<a href="https://greatdevelopers.github.io/ScriptCAD" class="w3-bar-item w3-button">Home</a>
<a href="https://goo.gl/forms/YeDk8IqOeDLKQOtB2" class="w3-bar-item w3-button">Register Here</a>
<div class="w3-dropdown-hover">
<button class="w3-button">Menu</button>
<div class="w3-dropdown-content w3-bar-block w3-card-4">
<a href="https://goo.gl/forms/YeDk8IqOeDLKQOtB2" class="w3-bar-item w3-button">Register Here</a>
<a href="https://groups.google.com/forum/#!forum/greatbim" class="w3-bar-item w3-button">GreatBIM</a>
<a href="https://greatdevelopers.github.io/ScriptCAD/Payment.html" class="w3-bar-item w3-button">Transaction Details</a>
<a href="https://greatdevelopers.github.io/ScriptCAD/FAQ.html" class="w3-bar-item w3-button">FAQs</a>
<a href="https://greatdevelopers.github.io/ScriptCAD/Terms.html" class="w3-bar-item w3-button">Terms & Conditions</a>
</div>
</div>

<div class="w3-dropdown-hover">
<button class="w3-button">Sessions</button>
<div class="w3-dropdown-content w3-bar-block w3-card-4">
<a href="https://greatdevelopers.github.io/ScriptCAD/Session0/Session0.html" class="w3-bar-item w3-button">Session-0</a>
<a href="https://greatdevelopers.github.io/ScriptCAD/Bishop_Tutorial.html" class="w3-bar-item w3-button">Session-1</a>
</div>
</div>

<div class="w3-dropdown-hover">
<button class="w3-button">Details</button>
<div class="w3-dropdown-content w3-bar-block w3-card-4">
<a href="http://cln2xdzm649l26znp2bl.gndec.sandcats.io:6080/index.html" class="w3-bar-item w3-button">Presentation</a>
<a href="https://lab.gdy.club/~suraj/sphinx/build/html/GameOfLife.html" class="w3-bar-item w3-button">Detailed Information</a>
<a href="http://guru.gndec.ac.in/course/view.php?id=102" class="w3-bar-item w3-button">Assignment</a>
</div>
</div>

</div>

# A Date with Python!

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
