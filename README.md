# Disclaimer
* This project is only for personal challenge and educational purpose, no other pretention than those ones.
* I could have used some libs such as [pyevolve](http://pyevolve.sourceforge.net/) but the goal was more
to understand how it works, what I am doing and why I am doing it.
* Objective was also to improve my personal skills in Python but perhaps sometimes my choices/approaches 
are not so 'pythonic', sorry about that.

# Overwiew
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