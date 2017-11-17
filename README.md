# Bayesian Network #

This repo is for University of Kentucky's CS463G bayesian assignment.

## Conditional Probability Table ##
Below are the conditional probability tables for variables A,B,D,E. Math
behind some of these probabilities are attached. See images in `math/` for
details.

Just a quick mention, I would like to thank Edwin Gogzheyang, Aidan Morgan,
and Kshitijia Taywade for some of these results, more detail in
Acknowledgement section.

|  Conditions  | Probability |
|--------------|-------------|
| P(A/B,C,D)   |   0.8873    |
| P(A/!B,C,!D) |   0.8571    |
| P(A/B,C,!D)  |   0.9921    |
| P(A/!B,C,D)  |   0.2727    |

|  Conditions  | Probability |
|--------------|-------------|
| P(B/A)       |     0.7     |
| P(B/!A)      |     0.1     |

|  Conditions  | Probability |
|--------------|-------------|
| P(D/A,C,E)   |   0.027     |
| P(D/!A,C,!E) |   0.973     |
| P(D/A,C,!E)  |   0.6923    |
| P(D/!A,C,E)  |   0.3077    |

|  Conditions  | Probability |
|--------------|-------------|
| P(E/C,D)     |     0.1     |
| P(E/C,!D)    |     0.9     |

## English Description ##
For the project, I first obtained conditional probabilities for
variable A, B, D and E, given that C is true. Please refer to the CPT below,
but essentially for every variable except C, we first find its Markov blanket,
then compute its probability with different combination of truth assignments
of the Markov blanket variables. For all the combinations, we keep C to be
true as it is a given.

I was able to hand-calculate conditional probabilities for variables A, B and
E thanks to Aidan Morgan's discussion post. For D it is fairly complicated
with a lot more math, so I only calculated a portion of the probability
formula and then referred to Kshitijia's discussion post results
along with results from a bayesian network simulator. I also confirmed that
the partial results I obtained for D matches with results from the simulator.

After the CPT is obtained, I set forth to find P(B|C=T) with MCMC simulation.
At the beginning of the simulation, every variable except C is at a random
state (true or false), with C being always true. At every step, variables get
updated one by one by first finding its probability of being true with the
calculated CPT, and then using a biased number generator, the program
determines whether the variable becomes true or not. For example, to find A's
next state, we look at B, C and D's current state. Since they are all true, we
see that P(A|B,C,D) = 0.8873, so A has a 88.73% chance of becoming true.

Throughout the simulation, we keep track of how many times B evaluates to
true. We then divide the count by the number of iterations so far to obtain
the probability of B given C=T. I perform this division every 1000 iterations,
with 10,000 total iterations.

5 runs are performed, and the results are graphed in the plot named 10000.png

As extra, I increased the number of iterations to 500,000, and then graphed
P(B|C=T) every 1,000 iterations. Results for that is in the plot named
500000.png. This is for reference only, but more iterations do make the graph
nicer, with the convergence more obvious.

## Patterns ##
For all the runs, they roughly converge into the value 0.59, with some
variations depending on how many iterations are performed. The more iterations
the more obvious the convergence is. As confirmed by the discussion group,
0.59 is the true P(B|C=T) as calculated through algebra, thus the simulation
is successful.

## Learning Outcome ##
Through this assignment, I have a deeper understanding of probabilities of a
variable in relation with other variables. It took me a while to understand
when to use Baye's theorem and when to not, I just have an autonomous response
to use the theorem whenever I see a "|", and get stuck in a loop of
probabilities. Now I know not to overthink the problem, and everything
logically makes sense.

## Acknowledgement ##
I would like to thank Edwin Gogzheyang for working with me on this assignment
and doubled checked with me on some conditional probabilities.

I would like to thank Aidan Morgan for explaining in a discussion post the
process of finding conditional probabilites for A. I instantly grasped the
concept and was able to find the rest of the probabilities.

Last but not least, I would like to thank Kshitija Taywade for sharing her
probabilities for variable D. Due to time constraint and tediousness, I only
partially solved the CPT for D. I was able to confirm her values through a
Bayesian network simulator, and used her values for the simulation.
