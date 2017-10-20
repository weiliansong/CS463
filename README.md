# README #
As this is a Markdown file, feel free to view it in a Markdown viewer, like
the one below!

https://dillinger.io/

## Get Started ##
I have implemented three SAT solving algorithms, and they are:

1. WalkSAT
2. Genetic
3. DPLL

All solvers are written in python 2.7, using these libraries:

1. numpy (for simplifying some tasks)
2. matplotlib (for making plots)

To solve a single formula, type  
`python main.py -f path/to/input/file`  
where `-f` argument specifies the input file, which should be in CNF form.  

To speed up the solving of the formulas, if you're using linux, you can
install parallel and parallelize the solving of the formulas. Follow the steps
below:

1. `apt-get install parallel`
2. `cd driver`
3. `chmod u+x driver.sh runner.sh`
4. `bash ./driver.sh cnf.list`

This will start as many jobs as you have CPU cores, replacing a completed job
with a new one as soon as one is finished.

Just to demonstrate that graphing works, you can run all the formulas and
generate fake data for plotting purposes. To do so, for step 4, run 
`bash ./driver.sh cnf_fake.list` instead.

Regardless of how you run jobs, there will be three folders created in the
root of the project folder, `stats_WalkSAT/`, `stats_Genetic/` and
`stats_DPLL/`.  Each folder represents the method of choice, and within each
folder will be a bunch of CSVs, whose names will be the names of the CNF
formula and within each contains runtime and fitness information for the
specified formula.

Once the three folders are somewhat populated, you can visualize the data you
collected by running `python visualize.py`, in which 6 plots will be created,
three are about runtime of each algorithm and the other three are about max
fitness found for each formula for each algorithm.

## Algorithms ##

### WalkSAT ###
Below is pseudocode for my WalkSAT program. Please refer to `walkSAT.py` for
full implementation details.

    for i = 1 -> MAX ITER
      Generate random variable assignments

      for j = 1 -> MAX FLIP
        if we solved all clauses
          return True
        else
          if current fitness > max fitness
            max fitness = current fitness
        
        find all unsatisfied clauses

        flip a coin
        
        if coin == head
          find the best variable to flip that maximizes fitness
          flip the assignment of the variable

        if coin == tail
          choose random variable from unsatisfied clauses
          flip the assignment of the random variable

      return False

I have set `MAX ITER = 100` and `MAX FLIP = 1000`. WalkSAT finds
satisfiability in a very reasonable amount of time, with worse case less than
100 seconds, solving 100-variable 400+ clause formulas. Included directory 
stats_WalkSAT contains actual statistics collected from solving formulas using
this algorithm.

### Genetic ###
Below is pseudocode for my Genetic program. Please refer to `genetic.py` for
full implementation details.

    for i = 1 -> MAX ITER
      Generate a population of random assignments of size TARGET POPULATION SIZE

      last best fitness = 0
      stagnation = 0

      for j = 1 -> MAX GEN
        Find fitnesses of all individuals of population
        
        if one member of population solves all clauses
          return True
        else
          if current best fitness > last best fitness
            last best fitness = current best fitness
            stagnation = 0

          else
            stagnation++
          
          if stagnation > GEN LIMIT
            exit to jump out of local min
          
        sort population by their fitness
        
        retain top SURVIVAL_RATE percent of population
        
        for k = 0 -> TARGET POPULATION SIZE - current population size
          first, second = pick two individuals from population weighted by fitness
          crossover between first and second CROSSOVER RATE percent of the times
          mutate offspring by MUTATE PERCENT, MUTATE RATE percent of the times
          add offspring into population

    return False

Below are the set of parameters I used:

MAX ITER = 50  
MAX GEN  = 500  
GEN LIMIT = 100  
TARGET POPULATION SIZE = 200  
SURVIVAL RATE = 10%  
CROSSOVER RATE = 50%  
MUTATE RATE = 40%  
MUTATE PERCENT = 5%  

My Genetic implementation is correct and works fine on small instances, but it
takes way too long on 100-variable 400+ clause instances, therefore I do not
have the time to run and analyze them. Some dummy stats files are used to
demonstrate the plotting feature, and please run the synthetic benchmark to
see it in live action.

### DPLL ###
Below is pseudocode for my DPLL program. Please refer to dpll.py for full
implementation details.

    function DPLL(clauses)
      if we solved all clauses
        return True
      
      if there exists an empty clause in clauses
        return False
      
      for variable in clauses
        if variable is pure
          remove all clauses that has the pure variable

      if we found pure variables
        DPLL(clauses)

      for variable in clauses
        if variable is in a unit clause
          remove all clauses that has the unit clause variable
          remove all appearances of the negation of the unit clause variable

      if we found unit clauses
        DPLL(clauses)

      lucky variable = random variable from clauses
      
      return DPLL(clauses(lucky variable = True)) or DPLL(clauses(lucky variable = False))

In my implementation, wherever I remove a clause, I basically mean that the
clause will evaluate to true because of one variable set to true, therefore
not needed to be considered anymore.

DPLL returns true if we don't have any more clauses to consider, meaning that
all of them are satisfied. DPLL returns false if one of the clause is empty,
meaning that variables are assigned in a way that can't make the specific
clause true, therefore overall not satisfied.

My DPLL implementation is correct and works fine on small instances, but it
takes way too long on 100-variable 400+ clause instances, therefore I do not
have the time to run and analyze them. Some dummy stats files are used to
demonstrate the plotting feature, and please run the synthetic benchmark to
see it in live action.

## Learning Outcome ##
From this assignment, I have learned three unique algorithms for solving
satisfiability. In terms of simplicity, I think DPLL is very straightforward
and elegant. In terms of speed, WalkSAT definitely takes the cake as it's the
only one that finished. Finally in terms of coolness, genetic algorithm is
entreating to write as it utilize the concept of evolution in an interesting
way.

What I also learned from this assignment is that naive implementation of these
algorithms often cannot find a solution in a reasonable amount of time. For
future implementations, I would research more about speed-ups and
short-circuiting techniques that I can use.

Finally, what I learned from this assignment is that parallelism within each
algorithm might not be benefical, as the overhead of creating multiple
processes might be longer than if you just execute jobs in sequence.
However, solving several formulas at once is very handy, as each solve is long
enough that the overhead of multiprocessing is negated.
