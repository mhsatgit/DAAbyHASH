# Experiment 10 - Improving Quick Sort Efficiency using Randomized Algorithm

## Aim

To implement and compare Deterministic Quick Sort and Randomized Quick Sort and analyze their performance for different types of input data.

## Problem Statement

Implement Quick Sort using:

1. Deterministic pivot selection
2. Randomized pivot selection

Compare their performance for:

- Random input
- Sorted input
- Reverse sorted input
- Nearly sorted input

The experiment uses an input size of 5000 elements.

## Description

Quick Sort is a divide-and-conquer sorting algorithm.

In Deterministic Quick Sort, the pivot is selected using a fixed strategy. In this experiment, the last element is selected as the pivot.

In Randomized Quick Sort, the pivot is selected randomly before partitioning.

Randomized pivot selection helps reduce the possibility of repeatedly selecting a poor pivot, especially when the input has an unfavorable ordering.

## Input

Input Size:

N = 5000

The following four types of arrays are tested:

### 1. Random

Contains randomly generated integer values.

### 2. Sorted

Contains elements already arranged in ascending order.

### 3. Reverse

Contains elements arranged in descending order.

### 4. Nearly Sorted

Contains an initially sorted array with a small number of random swaps.

## Algorithms

### Deterministic Quick Sort

1. Select the last element as the pivot.
2. Partition the array around the pivot.
3. Recursively sort the left subarray.
4. Recursively sort the right subarray.

### Randomized Quick Sort

1. Select a random element as the pivot.
2. Swap the random pivot with the last element.
3. Partition the array.
4. Recursively sort the left subarray.
5. Recursively sort the right subarray.

## Performance Measurement

The program measures:

- Number of comparisons
- Execution time in milliseconds

for both algorithms on all four input types.

## Complexity Analysis

| Algorithm | Average / Expected | Worst Case | Space |
|-----------|--------------------|------------|-------|
| Deterministic Quick Sort | O(n log n) | O(n²) | O(log n) |
| Randomized Quick Sort | O(n log n) | O(n²) | O(log n) |

## Output

The program displays a comparison table containing:

- Input type
- Deterministic Quick Sort comparisons
- Deterministic Quick Sort execution time
- Randomized Quick Sort comparisons
- Randomized Quick Sort execution time

## Conclusion

Randomized Quick Sort reduces the probability of repeatedly choosing poor pivots.

This makes it more robust than a deterministic pivot strategy when the input may be sorted, reverse sorted, or adversarial.

The experiment demonstrates how randomization can improve the practical performance of a divide-and-conquer algorithm.
