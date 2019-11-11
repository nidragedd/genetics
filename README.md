# DISCLAIMER
* This project is only for personal challenge and educational purpose, no other pretention than those ones.
* I could have used some libs such as [pyevolve](http://pyevolve.sourceforge.net/) but the goal was more
to understand how it works, what I am doing and why I am doing it.
* Objective was also to improve my personal skills in Python but perhaps sometimes my choices/approaches 
are not so 'pythonic', sorry about that.

# OVERVIEW
Goal of this project is to solve problems by using genetic algorithms.  
So far the problems to solve are:
* [sudoku](sudoku.md)
* some other to come later (maybe)


## GA pseudo-algorithm used
[Source](http://micsymposium.org/mics_2009_proceedings/mics2009_submission_66.pdf)
```
generate initial population
repeat
    rank the solutions, and retain only the percentage specified by selection rate
    repeat
        randomly select two solutions from the population
        randomly choose a crossover point
        recombine the solutions to produce n new solutions
        apply the mutation operator to the solutions
    until a new population has been produced
until a solution is found or the maximum number of generations is reached
```


---
## TECHNICAL PART
### Dependencies & Installation
Basically, this project requires **Python 3.7** in addition to [numpy](https://www.numpy.org/) package.

### Directory & code structure
Here is the structure of the project:
```
    project
      |__ objects    (contains classes)
      |__ samples    (contains .txt files to load)
      |__ sudoku     (utility functions to work with GA and sudokus)
      |__ tests      (unit and integration testing)
      |__ utils      (helper functions for the whole program)
      main.py        (the main script to launch)
```

### Run the app on your local computer
Run the following commands in the project's root directory:
    `python main.py --population-size 10000 --selection-rate 0.2 --random-selection-rate 0.2 --children 5 --mutation-rate 0.3 --max-generations 500 --pencil-mark True --model 4x4-beginner --restart-nb-generations 40`

Of course, adapt the parameters to the values you want to set. 