#                       SHORTEST PATH OUT OF THE MAZE

## This project works on finding the shortest route out of the maze

This project finds and displays the shortest path out of the maze. It works on Python language .

* This project uses python language
* It uses OOPs concepts to implement A* algorithm 
* We use weighted graphs for the shortest path and a heuristic function .

## CONCEPTS USED 

Some basic definitions needed to understand the project:

Graph - A non-linear data structure made using nodes(points) and edges.
Basically, It is bunch of points connected by edges . 

Weighted graph - In our context, this is the distance of the node(cell in the maze) to the end point. We consider the minimum value.

Heuristic Function - It estimates the distance from a cell in maze to the end cell.
For this algorithm , we need a heuristic that underestimates this distance.

Priority Queue - It is similar to a queue of people waiting with different priority . It is a list
of 2 value tuples;(element,priority). For this algo we just pop the least f after visiting it.

## Algorithm of A*

It is a simple method where we see that what distance have I travelled and what is left to travel.
We use the queue to see the minimum distance i have left to travel and stored it in a list . then i reverse track the list and print it.

We use oops for tracking each cell, making the choice , using the heuristic properly - manhattan distance(we donot have diagonal movement).


## Implementation 


