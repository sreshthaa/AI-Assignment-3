# AI-Assignment-3
<br>

// all the python code files are attached to the rpeosorot


1)When actions have different costs in a state based search space, an obvious choice is to use best-first search where the evaluation function is the cost of the path from the root to the current node. This is called Dijkstra’s algorithm by the theoretical computer science community, and uniform-cost search Uniform-cost search by the AI community. Implement the Dijkstra’s algorithm to all the cities in India and their Road distances. This info may be taken from open sources.

what the code does: 
-It uses Dijkstra’s Algorithm (Uniform Cost Search) to find shortest distance between cities connected by roads. Each city is treated as a node and distances between cities are edge weights.

Input:
-A graph (dictionary with cities and distances)
-A starting city

Process:
-Calculates shortest distance from the start city to all other cities
-Uses a priority queue for efficient selection

Output:
-Minimum distance from stat city to all other cities

<img width="1616" height="784" alt="image" src="https://github.com/user-attachments/assets/bd8ee5ca-65c0-4aa7-a195-69572eedfeec" />




2)An Unmanned Ground Vehicle (UGV) is a robot that finds the optimal path from a given user-specified start node to a user-specified Goal node on a map of a small area in a battlefield (Eg 70x70 Kms). There are obstacles known a-priori. The density of the obstacles can be generated randomly with three different levels of density. Design an algorithm that makes the UGV to navigate through this grid space avoiding all the known obstacles to reach the goal by the shortest distance. Trace this path along with the Measures of Effectiveness.

what the code does: 
-It simulates a UGV moving in a grid using the A* algorithm. It avoids obstacles and finds the shortest path from start to goal.

Input:
-Grid (2D list)
-Start position
-Goal position
-Obstacles (1 = blocked,0 = Unblocked)

Process:
-Finds shortest path using A* Algorithm
-Uses Manhattan distance as heuristic

Output
-Path (as a list of coordinates)
<img width="1621" height="774" alt="image" src="https://github.com/user-attachments/assets/45bc1b4d-93c9-4cb8-b36a-7691db87d221" />



3)In the above problem, we relax the condition that all obstacles are Static. In a real world, obstacles can be dynamic and not known a priori. How do you make the UGV navigate and find the optinal path in a dynamic obstacles environment.

what the code does: 
- extends the UGV problem to handle dynamic obstacles. The robot replans its path at every step when new obstacles appear

Input:
-Grid (2D list)
-Start position
-Goal position
-Obstacles (1 = blocked,0 = Unblocked)

Process:
-Moves step-by-step
-Runs A* again if environment changes
-Adds random obstacles

Output: 
-Final path taken (may differ from optimal solution)
<img width="1616" height="786" alt="image" src="https://github.com/user-attachments/assets/261b6534-f600-4ca3-9f1a-0c70affc9dae" />


