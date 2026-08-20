import heapq
from itertools import permutations


INF = float("inf")


def reduce_matrix(mat):
    """Reduce matrix and return reduction cost."""

    m = [row[:] for row in mat]
    n = len(m)
    cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(m[i])

        if row_min != INF and row_min != 0:
            cost += row_min

            for j in range(n):
                if m[i][j] != INF:
                    m[i][j] -= row_min

    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))

        if col_min != INF and col_min != 0:
            cost += col_min

            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost


def tsp_brute_force(cost, n):
    """Brute force method for verification."""

    cities = list(range(1, n))

    best_cost = INF
    best_path = None

    for perm in permutations(cities):

        path = [0] + list(perm) + [0]

        total_cost = 0

        for i in range(n):
            total_cost += cost[path[i]][path[i + 1]]

        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path

    return best_path, best_cost


def main():

    # 5-city cost matrix
    cost = [
        [INF, 10, 8, 9, 7],
        [10, INF, 10, 5, 6],
        [8, 10, INF, 8, 9],
        [9, 5, 8, INF, 6],
        [7, 6, 9, 6, INF]
    ]

    n = 5

    cities = ["A", "B", "C", "D", "E"]

    # Display input
    print("========== TSP INPUT ==========")
    print("Number of Cities :", n)

    print("\nCost Matrix:")

    print(f"{'':>5}", end="")

    for city in cities:
        print(f"{city:>6}", end="")

    print()

    for i, row in enumerate(cost):

        print(f"{cities[i]:>5}", end="")

        for value in row:

            if value == INF:
                value = "INF"

            print(f"{str(value):>6}", end="")

        print()

    # Find optimal path
    best_path, best_cost = tsp_brute_force(cost, n)

    # Display optimal tour
    print("\n========== OPTIMAL TOUR ==========")

    tour = " -> ".join(
        cities[i] for i in best_path
    )

    print("Optimal Tour :", tour)
    print("Minimum Cost :", best_cost)

    # Path verification
    print("\n========== PATH VERIFICATION ==========")

    for i in range(n):

        u = best_path[i]
        v = best_path[i + 1]

        print(
            f"{cities[u]} -> {cities[v]} : "
            f"Cost = {cost[u][v]}"
        )

    # Complexity
    print("\n========== COMPLEXITY ANALYSIS ==========")

    print("Brute Force Time Complexity : O((n-1)!)")
    print("Branch and Bound             : Exponential in worst case")
    print("Space Complexity             : O(n²)")

    # Result
    print("\n========== RESULT ==========")

    print(
        f"The optimal tour is {tour} "
        f"with a minimum total cost of {best_cost}."
    )


if __name__ == "__main__":
    main()