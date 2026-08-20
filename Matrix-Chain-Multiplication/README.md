# Experiment 6 - Matrix Chain Multiplication using Dynamic Programming

## Aim

To implement the Matrix Chain Multiplication algorithm using Dynamic Programming and find the optimal parenthesization that minimizes the total number of scalar multiplications.

## Problem Statement

Given a chain of 4 matrices with dimensions:

- A1 = 10 x 30
- A2 = 30 x 5
- A3 = 5 x 60
- A4 = 60 x 10

Find the optimal order of multiplication using Dynamic Programming and determine the minimum number of scalar multiplications required.

## Description

Matrix Chain Multiplication is a Dynamic Programming problem.

The order in which matrices are multiplied can significantly affect the number of scalar multiplications required.

The matrices cannot be rearranged. Only the placement of parentheses can be changed.

For example:

(A1 x A2) x A3

and

A1 x (A2 x A3)

represent different multiplication orders and may have different costs.

The Dynamic Programming approach calculates the minimum multiplication cost for every possible subchain and stores the optimal split position.

## Input

The matrix dimensions are:

A1 = 10 x 30
A2 = 30 x 5
A3 = 5 x 60
A4 = 60 x 10

The dimension array used is:

[10, 30, 5, 60, 10]

## Algorithm

1. Create a cost table `m` to store the minimum multiplication cost.
2. Create a split table `s` to store the optimal split position.
3. Consider chains of increasing length.
4. Try every possible split position for each chain.
5. Calculate the multiplication cost for every split.
6. Store the minimum cost and corresponding split position.
7. Reconstruct the optimal parenthesization using the split table.
8. Display the minimum multiplication cost and optimal order.

## Output

The program displays:

- Input matrices
- Matrix chain
- Optimal parenthesization
- Minimum number of scalar multiplications
- Dynamic Programming cost table
- Time and space complexity

## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | O(n^3) |
| Space Complexity | O(n^2) |

where `n` is the number of matrices.

## Files

- `matrix_chain.py` - Python implementation of Matrix Chain Multiplication.
- `output.txt` - Sample execution output.
- `screenshots/program_output.png` - Screenshot of the program output.

## Conclusion

The Dynamic Programming approach successfully determines the optimal order of multiplying the matrices while minimizing the total number of scalar multiplications.

Matrix Chain Multiplication demonstrates how Dynamic Programming avoids repeatedly solving the same subproblems by storing previously calculated results.
