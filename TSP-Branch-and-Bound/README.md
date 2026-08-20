# Experiment 8 - Travelling Salesman Problem using Branch and Bound

## Aim

To implement the Travelling Salesman Problem (TSP) using the Branch and Bound technique and find the optimal tour with minimum total cost.

## Problem Statement

Given a 5-city TSP with a known cost matrix, find the minimum cost Hamiltonian cycle using Branch and Bound with a lower-bound estimation based on reduced cost matrices.

The tour must:

- Visit every city exactly once.
- Return to the starting city.
- Have minimum possible total cost.

## Description

The Travelling Salesman Problem is an optimization problem in which a salesman must visit every city exactly once and return to the starting city while minimizing the total travel cost.

Branch and Bound reduces the search space by calculating lower bounds for partial solutions and pruning paths that cannot produce a better solution.

The experiment also uses brute-force enumeration for verification of the optimal result.

## Input

The problem contains 5 cities:

A, B, C, D, E

### Cost Matrix

|   | A | B | C | D | E |
|---|---:|---:|---:|---:|---:|
| A | INF | 10 | 8 | 9 | 7 |
| B | 10 | INF | 10 | 5 | 6 |
| C | 8 | 10 | INF | 8 | 9 |
| D | 9 | 5 | 8 | INF | 6 |
| E | 7 | 6 | 9 | 6 | INF |

## Algorithm

1. Represent the cities using a cost matrix.
2. Calculate lower bounds using matrix reduction.
3. Generate possible branches from the current city.
4. Calculate the lower bound for each branch.
5. Select the branch with the smallest bound.
6. Prune branches whose bound cannot improve the current best solution.
7. Continue until a complete tour is obtained.
8. Return to the starting city.
9. Display the optimal tour and its total cost.

## Output

The program displays:

- Number of cities
- Cost matrix
- Optimal tour
- Minimum tour cost
- Cost of each edge in the selected tour
- Complexity information

## Result

Optimal Tour:

A -> E -> B -> D -> C -> A

Minimum Cost:

34

## Complexity Analysis

The Travelling Salesman Problem is NP-Hard.

| Approach | Complexity |
|----------|------------|
| Brute Force | O((n-1)!) |
| Branch and Bound | Exponential in worst case |

Branch and Bound can significantly reduce the practical search space by pruning suboptimal branches.

## Files

- `tsp_branch_bound.py` - Python implementation of the TSP.
- `output.txt` - Sample execution output.
- `screenshots/program_output.png` - Screenshot of the program output.

## Conclusion

The Branch and Bound technique can efficiently prune suboptimal paths while searching for the optimal Hamiltonian cycle. For the given 5-city problem, the optimal tour is A -> E -> B -> D -> C -> A with a minimum total cost of 34.
