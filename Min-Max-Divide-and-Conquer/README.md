# Experiment 5 - Min-Max using Divide and Conquer

## Aim

To implement the Divide and Conquer approach to simultaneously find the minimum and maximum elements in an array and compare it with the naive linear approach in terms of the number of comparisons.

## Problem Statement

Given an array of n integers, find both the minimum and maximum values using the Divide and Conquer strategy.

Count and compare the number of comparisons made by the Divide and Conquer method versus the naive approach for arrays of size 10, 100, 1000, and 10000.

## Description

The Divide and Conquer approach divides the array into smaller parts until each part contains one or two elements.

The minimum and maximum values are then obtained by combining the results from the left and right halves.

The experiment also implements a naive approach that scans the entire array and compares each element with the current minimum and maximum.

## Algorithms Implemented

1. Divide and Conquer Min-Max
2. Naive Min-Max

## Input

A sample array is used for demonstration:

[3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

For performance analysis, randomly generated arrays of sizes:

- 10
- 100
- 1000
- 10000

are used.

## Output

The program displays:

- Input array
- Minimum value
- Maximum value
- Number of comparisons using Divide and Conquer
- Number of comparisons using the Naive approach
- Comparison counts for different input sizes
- Theoretical comparison formula

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| Divide and Conquer | O(n) | O(log n) |
| Naive | O(n) | O(1) |

## Comparison Formula

For the Divide and Conquer approach, the number of comparisons is:

3n/2 - 2

For the Naive approach, the number of comparisons is:

2(n - 1)

## Performance Analysis

| Size | D&C Comparisons | Naive Comparisons | Formula 3n/2 - 2 |
|------|-----------------|-------------------|-------------------|
| 10 | 13 | 18 | 13 |
| 100 | 148 | 198 | 148 |
| 1000 | 1498 | 1998 | 1498 |
| 10000 | 14998 | 19998 | 14998 |

## Conclusion

The Divide and Conquer approach successfully finds the minimum and maximum elements using fewer comparisons than the naive approach.

The Divide and Conquer method uses approximately 3n/2 - 2 comparisons, while the naive method requires 2(n - 1) comparisons.

For n = 10000, the Divide and Conquer method uses 14998 comparisons compared to 19998 comparisons for the naive approach, resulting in a 25% reduction in comparisons.
