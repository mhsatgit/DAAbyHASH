# Experiment 2 - Comparison of String Matching Algorithms

## Aim
To implement and compare the performance of three string matching algorithms: Naive String Matching, Knuth-Morris-Pratt (KMP), and Rabin-Karp.

## Description
String matching is the process of finding occurrences of a pattern within a given text. This experiment compares three popular algorithms based on the number of character comparisons required during pattern searching.

- **Naive Algorithm** checks every possible position in the text.
- **Knuth-Morris-Pratt (KMP)** uses a preprocessing step (LPS array) to avoid unnecessary comparisons.
- **Rabin-Karp** uses hash values to efficiently compare the pattern with substrings of the text.

## Algorithms Implemented
1. Naive String Matching
2. Knuth-Morris-Pratt (KMP)
3. Rabin-Karp

## Files
- `string_matching_comparison.py` – Python implementation of all three algorithms.
- `output.txt` – Sample execution output.
- `screenshots/program_output.png` – Screenshot of the program execution.

## Complexity Analysis

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Naive | O(n) | O(nm) | O(nm) | O(1) |
| KMP | O(n + m) | O(n + m) | O(n + m) | O(m) |
| Rabin-Karp | O(n + m) | O(n + m) | O(nm) *(hash collisions)* | O(1) |

where:
- **n** = length of the text
- **m** = length of the pattern

## Performance Analysis
The program compares the number of character comparisons performed by each algorithm on different pattern lengths using a randomly generated text of length 10,000. The comparison demonstrates the efficiency of KMP and Rabin-Karp over the Naive approach for larger inputs.

## Conclusion
The Naive algorithm is simple to implement but performs many redundant comparisons. KMP improves efficiency by utilizing the Longest Prefix Suffix (LPS) array, while Rabin-Karp uses hashing to quickly eliminate non-matching substrings. KMP generally provides the most consistent performance, whereas Rabin-Karp performs well unless many hash collisions occur.
