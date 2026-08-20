# Experiment 7 - N-Queens Problem using Backtracking

## Aim

To implement the N-Queens problem using the Backtracking technique in Python, find all valid solutions for N = 4, 6, and 8, and analyze the number of backtracks required.

## Problem Statement

Place N queens on an N × N chessboard such that no two queens attack each other.

No two queens should share:

- The same row
- The same column
- The same diagonal

The program finds all valid solutions for N = 4 and counts the total number of solutions and backtracks for N = 6 and N = 8.

## Description

The N-Queens problem is a classic constraint satisfaction problem.

Backtracking is used to place queens row by row. Before placing a queen, the program checks whether the position is safe.

If a position is not safe, it is skipped.

If a placement eventually leads to no valid solution, the algorithm removes the previously placed queen and tries another position.

This process continues until all possible solutions are found.

## Algorithm

1. Start with an empty N × N chessboard.
2. Begin placing queens from the first row.
3. Try each column in the current row.
4. Check whether the position is safe.
5. If the position is safe, place the queen.
6. Recursively move to the next row.
7. If no valid position is possible, backtrack and remove the previously placed queen.
8. Continue until all rows contain queens.
9. Record each valid solution.
10. Count the number of backtracks.

## Input

The program solves the problem for:

- N = 4
- N = 6
- N = 8

## Output

The program displays:

- Number of solutions
- Number of backtracks
- All solutions for N = 4
- Chessboard representation of the N = 4 solutions
- Complexity analysis

## Results

| N | Number of Solutions | Number of Backtracks |
|---|---------------------|----------------------|
| 4 | 2 | 26 |
| 6 | 4 | 152 |
| 8 | 92 | 876 |

## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | O(N!) |
| Space Complexity | O(N) |

## Conclusion

The Backtracking technique successfully solves the N-Queens problem by exploring possible queen placements and abandoning invalid partial solutions.

The number of backtracks increases rapidly as N increases, demonstrating the combinatorial nature of the N-Queens problem.
