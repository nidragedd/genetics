# Overwiew
Goal of this project is to solve problems by using genetic algorithms.  
So far the problems to solve are:
* sudoku
* some other to come later (maybe)

# Sudoku solver
### Approachs
With a 9 x 9 size, you should be able to solve the sudoku with another
approach than deploying a genetic algorithm: either brute force, pencil mark
and I am pretty sure that a lof of others exists if you have time for a little
googling session.
With greater size, it is not so easy and even for some 9 x 9 grids, sometimes
it is difficult to solve them *'logically'* and you need to bet on some answers
to move on.

### Why genetics may help
A genetic algorithm might find the solution quicker than trying all possible
solutions (after all, it is one of their goal) but it does not mean than it will
find the solution.  
It obviously depends on all parameters you will set (population size, number of
generations, mutation rate, etc).

### My approach
Highly similar to everything you can find on the internet related to sudoku solving
and genetic algorithms.  
Puzzles to solve are provided in a folder named ***"samples"***. They are stored
in plain text files containing the values where ***'|'*** character is the grid vertical separator
and ***'-'*** is the horizontal one. The ***'0'*** digit character is used to represent
and unknown value, so others are known as 'fixed' values. 

