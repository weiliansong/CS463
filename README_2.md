This README is for Puzzle 2 portion of the gear ball project.

# Solver #

## Solver Data Structure ##
For my solver, there are a few initialized variable before the main loop:

### frontier ###
this is the priority queue that will hold all states of the puzzle.
Within this python list are tuples of the form (state_priority, state).
state_priority is the cost so far + heuristic of state. When we pop frontier,
we are guaranteed to retrieve the best node so far with the highest priority
(smallest priority number).

### came_from ###
this is a python dict that represents traversed path of the
algorithm. Within the dict, each key value is a child, and each dict value to
a key is its parent. The form can be simplified as:
      came_from[child] = parent
I initialize came_from[start] = None, as the randomized state of the puzzle
has no parent node. Afterwards for each valid children of the parent state, I
set its parent to the parent state by `came_from[c_state] = p_state`. Once we
have a solution, we can trace the tree path by dictionary query until when we
reach None data field, which means we reached the top of the tree.

### cost_so_far ###
this is a python dict that contains the cost so far for each
visited state of the puzzle. This contains all the G scores of the states. The
cost for the beginning state of the puzzle is 0. When we reach a potential
neighbor, we first test to see if we have been to the same state before
(contains() function). If not, we immediately visit it and record the
cost_so_far + 1. Else if we have visited it before but the new cost is lower
than what we have before, we visit it again but update cost_so_far with the
lower cost. If the cost is higher than before, we simply ignore the move.

### final_state ###
this records the final state of the puzzle, which should be
solved other than the rotation of the edge pieces. This is mostly used to
traverse back through came_from and cost_so_far, as we need the exact object
to use as dictionary key.

### nodes_expanded ###
this counts the number of nodes expanded, as in number of times we pop from
the priority queue.

## Solver Algorithm ##
Implementation details of A\* is borrowed from Amit Patel's guide on search
algorithms. Here is the link: https://www.redblobgames.com/pathfinding/a-star/implementation.html#python-astar
Please see `a_star()` in `solver.py` for in-line comments about the
implementation of A\*.

# Heuristic #
In its essence, my heuristic computes the sum of all manhattan distances of
displacement of edge and corner pieces, and find the max between the two.
Before `max()` comparison, both values are divided by 8 as we can maximumly
displace 8 edges or 8 corners at a time. 

Note that my heuristic does not account for the orientation of the pieces nor
does it account for the correct rotation of the edge pieces. I do not account
for orientation because ultimately, if every piece is in its correct place,
then they should all be in its correct orientation as well. I do not account
for rotation of the edge pieces because it is trivial to solve the edge pieces
if every other piece is in place. All you have to do is move one face in a
specific direction for 4 times and the edges will be solved. Rinse and repeat
for each axis of unsolved edge pieces. See `fix_edges()` in `puzzle.py` for
details.

See `heuristic()` in `puzzle.py` for in-line comments.

# How to run code #
My program uses python3, numpy and matplotlib, all of which can be obtained
through Anaconda 3 if desired.

To run my program, simply type `python main.py` in a terminal or `run main.py`
in an iPython terminal.

Note: My heuristic and A\* is very slow, and does not solve efficiently for
some lower depth cases and cases with depth 6+, as they take over half an hour
to solve. I have the automated version of the code to try 5 k-randomized
puzzles, but that is commented out in `main.py`. Currently the code asks the
user for a k, makes a puzzle, randomizes it with k moves, and tries to solve
it.

# Commets on rotating pieces #
Since my GUI does not print out the position of the rotation of the center
edge pieces, I print them out instead in the console. To read them, hold the
cube in a certain way and look at the top and bottom center edge pieces
directly in front of you. They should lean the same direction as what's in
the console.

Lon edges: Look at the cube with blue face on left and green on right
Lat edges: Look at the cube with red face on left and purple on right
Cut edges: Look at the cube with yellow face on left and orange on right

# Learning Outcome #
This project has proven to be difficult, as I do not have a set-in-stone
heuristic to work with. I don't know if it is possible to solove for k > 6,
but I definitely wished to communicate with my peers more to discuss which
heuristic is correct.

This is my first time programming A\* from head to toe. The algorithm itself
is fairly intuitive, and I love how I can manipulate the algorithm to solve
things other than a maze.

Finally I learned a bit about runtime of gear ball solving algorithms. It
seems like everyone is hitting the time wall, with k >= 6 taking more than
half an hour to solve. Of course there is still a chance for bugs in my
program, but I can imagine that the complexity of the gear ball does not allow
it to be solved very quickly, similar to a rubik's cube.
