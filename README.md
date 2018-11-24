# Disclaimer
* This project is only for personal challenge and ecucational purpose, no other pretention than those ones.
* I could have used some libs such as numpy or [pyevolve](http://pyevolve.sourceforge.net/) but the goal was more
to understand how it works, what I am doing and why I am doing it.
* Objective was also to improve my personal skills in Python but perhaps sometimes my choices/approaches 
are not so 'pythonic', sorry about that

# Overwiew
Goal of this project is to solve problems by using genetic algorithms.  
So far the problems to solve are:
* sudoku
* some other to come later (maybe)

# Sudoku solver
### A lot of approaches are available
With a 9x9 size, you should be able to solve the sudoku with another
approach than deploying a genetic algorithm:
* brute force (well, only for small and easy grids)
* [pencil mark](https://www.learn-sudoku.com/pencil-marks.html)
* [backtracking](https://www.geeksforgeeks.org/sudoku-backtracking-7/)  

And I am pretty sure that a lof of others exists if you have time for a little googling session.

With greater size, it is not so easy and even for some 9x9 grids, sometimes
it is difficult to solve them *'just with logic'* and you need to bet on some answers
to move on.  
Extract from a good reading [here](http://micsymposium.org/mics_2009_proceedings/mics2009_submission_66.pdf):
*"The standard approach to computer-based Sudoku solvers is a generate-and-test solution using
backtracking. This strategy works extremely well for smaller grid sizes (including the
standard 9x9 grid configuration), but becomes computationally intractable for larger sizes. In
fact, the general problem of solving NxN Sudoku puzzles is known to be NP-complete"*

### So, why genetics ?
A genetic algorithm might find the solution quicker than trying all possible
solutions (after all, it is one of their goal) but it does not mean than it ***will***
find the solution.    
Compared to other approaches, genetic algorithm seems not being a good choice.
It obviously depends on all parameters you will set (population size, number of
generations, mutation rate, etc) and play with. With a large enough population size or number of generations,
it will/should most of the time solve the sudokus. But it happens sometimes, depending
on the difficulty level that the program gets stuck in local minima.
Then, there is no other choice than restarting it.  

As said earlier, solving NxN sudoku puzzle is a NP-complete in terms of complexity, that is why GA is a
good candidate, but not the best one (again, a little googling session and you will find a lot of documentations
regarding this topic).

### My approach
Highly similar to everything you can find on the internet related to sudoku solving
and genetic algorithms.  
Puzzles to solve are provided in a folder named ***"samples"***. They are stored
in plain text files containing the values. ***'|'*** character is the grid vertical separator
and ***'-'*** is the horizontal one. The ***'0'*** digit character is used to represent
an unknown value (so others are known and are so called 'fixed' values). 

### Pseudo-algorithm
[Source](http://micsymposium.org/mics_2009_proceedings/mics2009_submission_66.pdf)
```
generate initial population
repeat
    rank the solutions, and retain only the percentage specified by selection rate
    repeat
        randomly select two unused solution strings from the population
        randomly choose a crossover point
        recombine the solutions to produce two new solution strings
        apply the mutation operator to the solutions
    until a new population has been produced
until a solution is found or the maximum number of generations is reached
```

### Possible improvements
* When generating children, keep parents if their fitness is better