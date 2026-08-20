def first_fit(items, capacity=1.0):
    bins = []
    bin_contents = []

    for item in items:
        placed = False

        for i in range(len(bins)):
            if bins[i] + item <= capacity:
                bins[i] += item
                bin_contents[i].append(item)
                placed = True
                break

        if not placed:
            bins.append(item)
            bin_contents.append([item])

    return bin_contents


def first_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, capacity)


def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)

    bins = []
    bin_contents = []

    for item in sorted_items:
        best_bin = -1
        minimum_remaining = float("inf")

        for i in range(len(bins)):
            remaining = capacity - (bins[i] + item)

            if remaining >= 0 and remaining < minimum_remaining:
                minimum_remaining = remaining
                best_bin = i

        if best_bin != -1:
            bins[best_bin] += item
            bin_contents[best_bin].append(item)
        else:
            bins.append(item)
            bin_contents.append([item])

    return bin_contents


def display_bins(name, bins):
    print(f"\n========== {name} ==========")

    for i, bin_items in enumerate(bins, 1):
        total = sum(bin_items)

        print(
            f"Bin {i}: "
            f"{bin_items} "
            f"-> Used = {total:.1f}, "
            f"Remaining = {1.0 - total:.1f}"
        )

    print(f"Total Bins Used : {len(bins)}")


def main():

    items = [
        0.5, 0.7, 0.3, 0.9, 0.2,
        0.6, 0.8, 0.4, 0.1, 0.5
    ]

    capacity = 1.0

    # Theoretical lower bound
    total_weight = sum(items)
    lower_bound = int(total_weight / capacity)

    if total_weight % capacity != 0:
        lower_bound += 1

    print("========== BIN PACKING ==========")

    print(f"Items        : {items}")
    print(f"Bin Capacity : {capacity}")
    print(f"Total Weight : {total_weight:.1f}")

    print(
        f"Theoretical Lower Bound : "
        f"{lower_bound} bins"
    )

    # Apply approximation algorithms
    ff_bins = first_fit(items, capacity)
    ffd_bins = first_fit_decreasing(items, capacity)
    bfd_bins = best_fit_decreasing(items, capacity)

    # Display results
    display_bins(
        "FIRST FIT (FF)",
        ff_bins
    )

    display_bins(
        "FIRST FIT DECREASING (FFD)",
        ffd_bins
    )

    display_bins(
        "BEST FIT DECREASING (BFD)",
        bfd_bins
    )

    # Summary
    print("\n========== SUMMARY ==========")

    print(
        f"Lower Bound : {lower_bound} bins"
    )

    print(
        f"First Fit (FF)             : "
        f"{len(ff_bins)} bins"
    )

    print(
        f"First Fit Decreasing (FFD) : "
        f"{len(ffd_bins)} bins"
    )

    print(
        f"Best Fit Decreasing (BFD)  : "
        f"{len(bfd_bins)} bins"
    )

    print("\n========== COMPLEXITY ANALYSIS ==========")

    print("First Fit (FF)")
    print("Time Complexity  : O(n²)")
    print("Space Complexity : O(n)")

    print("\nFirst Fit Decreasing (FFD)")
    print("Time Complexity  : O(n²)")
    print("Space Complexity : O(n)")

    print("\nBest Fit Decreasing (BFD)")
    print("Time Complexity  : O(n²)")
    print("Space Complexity : O(n)")

    print("\n========== RESULT ==========")

    print(
        "The approximation algorithms successfully "
        "packed all items \ninto bins and were compared "
        "with the theoretical lower bound."
    )


if __name__ == "__main__":
    main()