# Experiment 4 - Single Source Shortest Path using Dijkstra's Algorithm

## Aim
To implement Dijkstra's Single Source Shortest Path algorithm to find the shortest distance and actual shortest path from a source vertex to all other vertices in a directed weighted graph.

## Problem Statement
Given a directed weighted graph with 6 vertices (0–5) and weighted edges, find the shortest path from source vertex 0 to all other vertices. Print the shortest distances and the actual path taken for each destination.

## Description
Dijkstra's Algorithm is a greedy algorithm used to find the shortest paths from a single source vertex to all other vertices in a weighted graph.

The algorithm repeatedly selects the unvisited vertex with the smallest known distance and updates the distances of its neighboring vertices.

## Algorithm
1. Initialize the distance of the source vertex as `0` and all other distances as infinity.
2. Select the unvisited vertex with the smallest distance.
3. Mark the selected vertex as visited.
4. Check all outgoing edges from the selected vertex.
5. Update the distance if a shorter path is found.
6. Store the previous vertex to reconstruct the shortest path.
7. Repeat until all reachable vertices are processed.
8. Display the shortest distance and actual path from the source to every destination.

## Input
- Number of vertices: `6`
- Vertices: `0, 1, 2, 3, 4, 5`
- Source vertex: `0`
- Directed weighted edges.

## Output
The program displays:
- Shortest distance from vertex `0` to every other vertex.
- Actual shortest path taken for each destination.

## Complexity Analysis

| Implementation | Time Complexity | Space Complexity |
|---|---|---|
| Dijkstra using Priority Queue | O((V + E) log V) | O(V + E) |

where:
- **V** = Number of vertices
- **E** = Number of edges

## Important Note
Dijkstra's Algorithm works correctly when all edge weights are non-negative. It should not be used when the graph contains negative edge weights.

## Files
- `dijkstra.py` – Python implementation of Dijkstra's Algorithm.
- `output.txt` – Sample execution output.
- `screenshots/program_output.png` – Screenshot of the program execution.

## Conclusion
Dijkstra's Algorithm efficiently finds the shortest paths from a single source vertex to all other vertices in a weighted graph with non-negative edge weights. By maintaining the shortest known distance and previous vertex for each node, the algorithm can also reconstruct the actual shortest path.
