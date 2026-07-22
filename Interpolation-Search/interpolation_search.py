import random
import time
import matplotlib.pyplot as plt

# Interpolation Search Function
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and key >= arr[low] and key <= arr[high]:
        comparisons += 1

        if arr[low] == arr[high]:
            if arr[low] == key:
                return low, comparisons
            return -1, comparisons

        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

        comparisons += 1
        if arr[pos] == key:
            return pos, comparisons

        comparisons += 1
        if arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


# Generate Uniformly Distributed Sorted Array
n = int(input("Enter number of elements: "))

arr = list(range(1, n * 10, 10))

print("\nGenerated Array:")
print(arr)

key = int(input("\nEnter element to search: "))

# Measure execution time
start_time = time.perf_counter()

position, comparisons = interpolation_search(arr, key)

end_time = time.perf_counter()

execution_time = (end_time - start_time) * 1e6  # microseconds

# Display Results
print("\n----- Search Result -----")

if position != -1:
    print(f"Element found at index: {position}")
else:
    print("Element not found")

print(f"Number of comparisons: {comparisons}")
print(f"Execution time: {execution_time:.4f} microseconds")

# Complexity Information
print("\n----- Complexity Analysis -----")
print("Best Case Time Complexity : O(1)")
print("Average Case Time Complexity : O(log log n)")
print("Worst Case Time Complexity : O(n)")
print("Space Complexity : O(1)")


# Performance Analysis for Different Input Sizes
sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
times = []

for size in sizes:
    test_arr = list(range(1, size * 10, 10))
    test_key = test_arr[len(test_arr) // 2]

    start = time.perf_counter()
    interpolation_search(test_arr, test_key)
    end = time.perf_counter()

    times.append((end - start) * 1e6)

# Plot Graph
plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o')
plt.title("Interpolation Search Performance")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (microseconds)")
plt.grid(True)
plt.show()