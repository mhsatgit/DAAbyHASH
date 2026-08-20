import random


comparison_count = 0


# Divide and Conquer Approach
def min_max_dc(arr, low, high):
    global comparison_count

    # Base case: single element
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]

        return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    # Combine
    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


# Naive Approach
def min_max_naive(arr):
    mn = arr[0]
    mx = arr[0]
    comparisons = 0

    for x in arr[1:]:
        comparisons += 1

        if x < mn:
            mn = x

        comparisons += 1

        if x > mx:
            mx = x

    return mn, mx, comparisons


def main():

    # Demonstration on small array
    arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

    global comparison_count

    comparison_count = 0

    mn, mx = min_max_dc(
        arr,
        0,
        len(arr) - 1
    )

    dc_comparisons = comparison_count

    _, _, naive_comparisons = min_max_naive(arr)

    print("========== INPUT ARRAY ==========")
    print(f"Array : {arr}")

    print("\n========== MIN-MAX RESULT ==========")
    print(f"Minimum Value : {mn}")
    print(f"Maximum Value : {mx}")

    print("\n========== COMPARISON COUNT ==========")
    print(f"Divide and Conquer Comparisons : {dc_comparisons}")
    print(f"Naive Approach Comparisons     : {naive_comparisons}")

    # Performance Analysis
    print("\n========== PERFORMANCE ANALYSIS ==========")

    print(
        f"{'Size':>8}"
        f"{'D&C Comparisons':>20}"
        f"{'Naive Comparisons':>20}"
        f"{'Formula 3n/2-2':>20}"
    )

    print("-" * 68)

    for size in [10, 100, 1000, 10000]:

        arr = [
            random.randint(1, 10000)
            for _ in range(size)
        ]

        comparison_count = 0

        mn, mx = min_max_dc(
            arr,
            0,
            len(arr) - 1
        )

        dc = comparison_count

        _, _, naive = min_max_naive(arr)

        formula = 3 * size // 2 - 2

        print(
            f"{size:>8}"
            f"{dc:>20}"
            f"{naive:>20}"
            f"{formula:>20}"
        )

    # Complexity Analysis
    print("\n========== COMPLEXITY ANALYSIS ==========")

    print("Divide and Conquer")
    print("Time Complexity  : O(n)")
    print("Space Complexity : O(log n)")

    print("\nNaive Approach")
    print("Time Complexity  : O(n)")
    print("Space Complexity : O(1)")

    # Result
    print("\n========== RESULT ==========")
    print(
        "The Divide and Conquer approach successfully "
        "found the minimum and maximum"
    )
    print(" values while using fewer comparisons than the naive approach.")


if __name__ == "__main__":
    main()