import random
import time
import sys

sys.setrecursionlimit(20000)

comparisons = 0


def partition(arr, low, high):
    global comparisons

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def deterministic_quicksort(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)

        deterministic_quicksort(
            arr, low, pi - 1
        )

        deterministic_quicksort(
            arr, pi + 1, high
        )


def randomized_quicksort(arr, low, high):
    if low < high:

        # Choose a random pivot
        random_index = random.randint(
            low, high
        )

        arr[random_index], arr[high] = (
            arr[high],
            arr[random_index]
        )

        pi = partition(arr, low, high)

        randomized_quicksort(
            arr, low, pi - 1
        )

        randomized_quicksort(
            arr, pi + 1, high
        )


def run_test(name, sort_function, arr):
    global comparisons

    test_array = arr[:]

    comparisons = 0

    start_time = time.perf_counter()

    sort_function(
        test_array,
        0,
        len(test_array) - 1
    )

    end_time = time.perf_counter()

    execution_time = (
        end_time - start_time
    ) * 1000

    return comparisons, execution_time


def main():

    N = 5000

    # Generate test cases
    test_cases = {
        "Random": [
            random.randint(1, 100000)
            for _ in range(N)
        ],

        "Sorted": list(range(N)),

        "Reverse": list(range(N, 0, -1)),

        "Nearly Sorted": list(range(N))
    }

    # Slightly shuffle the nearly sorted array
    nearly_sorted = test_cases["Nearly Sorted"]

    for _ in range(N // 20):

        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)

        nearly_sorted[i], nearly_sorted[j] = (
            nearly_sorted[j],
            nearly_sorted[i]
        )

    print("========== QUICK SORT COMPARISON ==========")
    print(f"Input Size : {N}")

    print(
        "\nComparing Deterministic Quick Sort "
        "and Randomized Quick Sort"
    )

    print("\n" + "-" * 85)

    print(
        f"{'Input Type':<18}"
        f"{'DQS Comparisons':>18}"
        f"{'DQS Time(ms)':>15}"
        f"{'RQS Comparisons':>18}"
        f"{'RQS Time(ms)':>15}"
    )

    print("-" * 85)

    for name, arr in test_cases.items():

        dqs_comparisons, dqs_time = run_test(
            name,
            deterministic_quicksort,
            arr
        )

        rqs_comparisons, rqs_time = run_test(
            name,
            randomized_quicksort,
            arr
        )

        print(
            f"{name:<18}"
            f"{dqs_comparisons:>18}"
            f"{dqs_time:>15.4f}"
            f"{rqs_comparisons:>18}"
            f"{rqs_time:>15.4f}"
        )

    print("\n========== COMPLEXITY ANALYSIS ==========")

    print("Deterministic Quick Sort")
    print("Average Time Complexity : O(n log n)")
    print("Worst Time Complexity   : O(n²)")
    print("Space Complexity        : O(log n)")

    print("\nRandomized Quick Sort")
    print("Expected Time Complexity : O(n log n)")
    print("Worst Time Complexity    : O(n²)")
    print("Space Complexity         : O(log n)")

    print("\n========== RESULT ==========")

    print(
        "Randomized Quick Sort reduces the probability "
        "of consistently selecting\n poor pivots and "
        "generally provides better\n performance on "
        "adversarial or already ordered inputs."
    )


if __name__ == "__main__":
    main()