# Experiment 9 - Efficient Bin Packing using Approximation Algorithm

## Aim

To implement and compare different Bin Packing approximation algorithms and evaluate their efficiency relative to the theoretical lower bound.

## Problem Statement

Given a set of items with weights:

[0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]

and bins with capacity 1.0, apply the following approximation algorithms:

1. First Fit (FF)
2. First Fit Decreasing (FFD)
3. Best Fit Decreasing (BFD)

Compare the number of bins used by each algorithm with the theoretical lower bound.

## Description

Bin Packing is an optimization problem where items of different sizes must be placed into bins of fixed capacity while minimizing the number of bins used.

Finding the exact optimal solution is computationally difficult. Therefore, approximation algorithms are used to obtain good solutions efficiently.

### First Fit

First Fit places each item into the first bin in which it fits.

If the item does not fit in any existing bin, a new bin is opened.

### First Fit Decreasing

First Fit Decreasing first sorts all items in decreasing order and then applies First Fit.

### Best Fit Decreasing

Best Fit Decreasing first sorts the items in decreasing order.

Each item is then placed into the bin that leaves the smallest remaining space while still fitting the item.

## Input

Items:

[0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]

Bin Capacity:

1.0

## Algorithms

### First Fit

1. Process items in their original order.
2. Check existing bins.
3. Place the item in the first bin where it fits.
4. If no bin can accommodate the item, open a new bin.

### First Fit Decreasing

1. Sort all items in decreasing order.
2. Apply the First Fit algorithm.
3. Count the number of bins used.

### Best Fit Decreasing

1. Sort all items in decreasing order.
2. Find the bin with the smallest remaining space where the item fits.
3. Place the item in that bin.
4. If no suitable bin exists, open a new bin.

## Output

The program displays:

- Input items
- Bin capacity
- Total weight
- Theoretical lower bound
- Bins produced by First Fit
- Bins produced by First Fit Decreasing
- Bins produced by Best Fit Decreasing
- Number of bins used by each algorithm
- Complexity analysis

## Theoretical Lower Bound

The minimum possible number of bins cannot be less than:

ceil(Total Weight / Bin Capacity)

For this problem:

Total Weight = 5.0

Bin Capacity = 1.0

Lower Bound = 5 bins

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| First Fit | O(n²) | O(n) |
| First Fit Decreasing | O(n²) | O(n) |
| Best Fit Decreasing | O(n²) | O(n) |

## Conclusion

The three approximation algorithms successfully pack all items into bins.

First Fit processes items in their original order, while First Fit Decreasing and Best Fit Decreasing first sort the items in decreasing order.

The algorithms are compared against the theoretical lower bound to evaluate how efficiently they use the available bins.

Bin Packing is an NP-Hard optimization problem, so approximation algorithms provide practical solutions for larger inputs.
