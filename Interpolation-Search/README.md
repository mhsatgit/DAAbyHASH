# Experiment 1 - Interpolation Search

## Aim
To implement the Interpolation Search algorithm in Python and analyze its performance by measuring the number of comparisons, execution time, and time complexity.

## Description
Interpolation Search is an efficient searching algorithm for sorted and uniformly distributed data. Unlike Binary Search, which always checks the middle element, Interpolation Search estimates the probable position of the target element based on its value, reducing the number of comparisons for uniformly distributed datasets.

## Algorithm
1. Initialize `low` as the first index and `high` as the last index.
2. While the key lies within the range of the current search interval:
   - Estimate the probable position (`pos`) using the interpolation formula.
   - If the element at `pos` matches the key, return its index.
   - If the element is smaller than the key, search the right half.
   - Otherwise, search the left half.
3. If the element is not found, return `-1`.

## Files
- `interpolation_search.py` – Python implementation of Interpolation Search.
- `output.txt` – Sample program output.
- `graph.png` – Performance graph showing execution time for different input sizes.

## Complexity Analysis

| Case | Time Complexity |
|------|-----------------|
| Best Case | O(1) |
| Average Case | O(log log n) |
| Worst Case | O(n) |
| Space Complexity | O(1) |

## Performance Analysis
The program records the execution time of Interpolation Search for different input sizes and plots a graph to visualize its performance. The algorithm performs exceptionally well on uniformly distributed sorted data, where its average time complexity is **O(log log n)**.

## Conclusion
Interpolation Search is faster than Binary Search for uniformly distributed sorted datasets because it predicts the likely position of the target element instead of always dividing the search space in half. However, its performance degrades to **O(n)** when the data is not uniformly distributed.
