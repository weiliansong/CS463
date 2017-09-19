# Gear Ball Puzzle #

## How to run this program ##
First, install these software/packages

* Python 2.7
* Numpy
* Matplotlib

Then go to the root folder of the project and type `python main.py`.

## Data Structure ##
The data structure consists of
* ball - one 6 x 3 x 3 matrix of values 0~5
* xxx_edges - four 1 x 4 vectors for edge pieces

### Ball Matrix ###
Within ball are six 3 x 3 matrices, each representing a face of the puzzle.
The faces of the gear ball are labelled as below:
* 0 - left
* 1 - front
* 2 - right
* 3 - back
* 4 - top
* 5 - bottom 

Note that the relationship is not defined by color, therefore any orientation
of the cube is fine as long as it is consistent throughout the simulation. I
do have a color map that maps numbers to color for testing purposes.

Below is how the cube is displayed in the GUI. Note that the number of x's is
irrelevant, as I only use enough of it to make a decently large shape to look
at.
          xxxxxxxxx
          xxxxxxxxx
          xxx 3 xxx
          xxxxxxxxx
          xxxxxxxxx

xxxxxxxxx xxxxxxxxx xxxxxxxxx
xxxxxxxxx xxxxxxxxx xxxxxxxxx
xxx 0 xxx xxx 4 xxx xxx 2 xxx
xxxxxxxxx xxxxxxxxx xxxxxxxxx
xxxxxxxxx xxxxxxxxx xxxxxxxxx

          xxxxxxxxx
          xxxxxxxxx
          xxxxxxxxx
          xxx 1 xxx
          xxxxxxxxx

          xxxxxxxxx
          xxxxxxxxx
          xxx 5 xxx
          xxxxxxxxx
          xxxxxxxxx

### Middle Edge Pieces ###
Rotating middle edge pieces are modeled with three vectors of length 4. There
are a total of 12 middle edge pieces, four in latitute direction, 4 in
longitude direction, and 4 in what I denote "cut" direction. 

Maybe a little bit easier to understand:
* lat_edges: middle edge pieces b/t top and bottom slice of a cube
* lon_edges: middle edge pieces b/t left tand right slice of a cube
* cut_edges: middle edge pieces b/t front and back slice of a cube

Within each vector, we place the number of degrees the piece is currently at
With every turn of a face, 4 edge pieces rotate 300 degrees in the
opposite direction of the turn face, and the other 8 edge pieces swap places.
Degrees are modded by 360 to make it easier to understand where it is at.

### Code ###
Code for the data structure is in puzzle.py. A puzzle object needs to be
created, which it will call a reset function at the beginning. Then to move
the puzzle, a face and a direction needs to be determined. Available faces to
turn are: Left, Front, and Top, and each of the three can be turned CW or CCW.
Reason for only three faces is that when holding the middle, turning left face
CW equals turning right face CW, therefore reducing the number of possible
turns.

## Randomizer ##
The randomizer I have takes as input the number of moves N, and outputs a
vector of length N with components m, specifying the face and direction to
turn. If N is 4, then the vector would look like...

[[4, 'ccw'], [0, 'cw'], [0, 'cw'], [1, 'ccw']]

To make a random move, a random face and a random direction is first chosen.
Then the program checks to see if it is exactly the opposite move it made
before. If not, then it checks to make sure it hasn't done the same move 6
times in a row. Finally the move passes inspection, and gets added to a global
set of moves to be used for the puzzle.

When making moves, the randomizer keeps track of the last move it made and
a counter indicating how many of the same moves it has made. When verifying
the new move, if it is equal to the last move, counter goes up by one. If this
counter gets above 6, then the randomizer discards the move and keep grabbing
a new one that is on a different face.

Code for the randomizer is within randomizer.py. An object of the Randomizer
class needs to be made and a move is retrieved by calling the
get_random_move() function.

## Heuristics ##
My heuristic the minimum of two numbers a and b. a is the maximum distance for a
single corner to return to its spot, and b is the maximum distance for any edge
from its belonged spot.

First, let me explain about a. For each corner, imagine we can pop the corner
piece out and move it according to manhattan rules to match its colors with
centers of the three faces it is connected with. I compute all corner's cost this 
way, and find the maximum of them all.  That should give the minimum number of 
moves it takes to solve the corners of the cube, as solving one might solve the 
other 7.

b is needed because a is only concerned with the corners, and we can't just
solve the cube without caring for its edges. Every edge belongs between two
middles, specifically the two that shares its colors.  We can tell at a glance
whether if it's already in place by looking at the two faces the edge
connects. We calculate the distance by imagining we can pop the edge and move
it according to manhattan rules. Note that we do not care for rotations here,
we just want to put it in its right spot. We calculate that cost for each
edge, and find the maximum among all.

This heuristic produces a lower bound, because the main difference between the
gear ball and a rubik's cube is that solving some corners might solve some
edges for you, and solving some edges might solve some corners. The lower of
the two should be the least amount of moves it takes, since we do not know
where the two sets of moves overlap.

## What I Learned ##
This project is interesting because it's the first time I tried to model a
puzzle. There were some design choices that probably shouldn't have been
picked, like using matplotlib to make the GUI. Thinking back, I should have
used just a regular figure drawing library so the rotating center edges can be
displayed more efficiently.

Something else I learned is the mindset of finding the least complicated way
to represent something. Modeling the ball with only three faces and two
rotational directions is much simpler than holding one side and rotate the
other side. I'm glad I made that design decision early on and saved a lot of
work.

Finally, I learned from this project numpy array indexing. I knew about this
functionality before, but after this assignment I am fairly comfortable
indexing a 3D array by any of its column, row, or the combination.
