# Experiment 3 - Comparison of Minimum Spanning Tree Algorithms

## Aim
To implement and compare Prim's and Kruskal's algorithms for finding the Minimum Spanning Tree (MST) of a weighted undirected graph.

## Description
A Minimum Spanning Tree (MST) is a subset of the edges of a connected, weighted, undirected graph that connects all vertices with the minimum possible total edge weight and without forming any cycles.

This experiment compares two popular MST algorithms:

- **Prim's Algorithm** – Grows the MST one vertex at a time by selecting the minimum-weight edge connecting a visited vertex to an unvisited vertex.
- **Kruskal's Algorithm** – Sorts all edges in increasing order of weight and adds them to the MST if they do not form a cycle, using the Union-Find (Disjoint Set) data structure.

## Algorithms Implemented
1. Prim's Algorithm
2. Kruskal's Algorithm

## Files
- `mst_comparison.py` – Python implementation of Prim's and Kruskal's algorithms.
- `output.txt` – Sample execution output.
- `screenshots/program_output.png` – Screenshot of the program execution.

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Prim's (using Priority Queue) | O(E log V) | O(V + E) |
| Kruskal's (using Union-Find) | O(E log E) | O(V) |

where:
- **V** = Number of vertices
- **E** = Number of edges

## Performance Analysis
Both algorithms generate the same Minimum Spanning Tree with the same total cost for a connected weighted graph.

- Prim's algorithm is generally preferred for **dense graphs**, especially when implemented with a priority queue.
- Kruskal's algorithm performs well for **sparse graphs** and efficiently avoids cycles using the Union-Find data structure.

## Conclusion
Both Prim's and Kruskal's algorithms correctly compute the Minimum Spanning Tree of a weighted graph. Although they follow different approaches, they produce an MST with the same minimum total cost. The choice between the two depends on the graph representation and its density.
