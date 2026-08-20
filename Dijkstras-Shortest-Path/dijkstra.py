import heapq


def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V + E)
    """

    n = len(graph)

    dist = [float("inf")] * n
    prev = [None] * n

    dist[source] = 0

    priority_queue = [(0, source)]

    visited = set()

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u]:

            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u

                heapq.heappush(
                    priority_queue,
                    (dist[v], v)
                )

    return dist, prev


def reconstruct_path(prev, source, target):

    path = []
    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


def main():

    # Directed weighted graph
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: [(5, 2)],
        5: []
    }

    source = 0

    # Display Input
    print("========== INPUT GRAPH ==========")
    print("Number of Vertices : 6")
    print(f"Source Vertex      : {source}")

    print("\nDirected Edges:")

    for u in graph:
        for v, weight in graph[u]:
            print(f"{u} -> {v}  Weight = {weight}")

    # Run Dijkstra's Algorithm
    dist, prev = dijkstra(graph, source)

    # Display Output
    print("\n========== DIJKSTRA'S ALGORITHM ==========")
    print(f"Shortest Paths from Source Vertex {source}")

    print("\n" + "-" * 55)
    print(f"{'Vertex':<10}{'Distance':<15}{'Shortest Path'}")
    print("-" * 55)

    for v in range(len(graph)):

        if dist[v] == float("inf"):
            distance = "INF"
            path = "No path"
        else:
            distance = dist[v]

            path_list = reconstruct_path(prev, source, v)

            path = " -> ".join(
                map(str, path_list)
            )

        print(f"{v:<10}{str(distance):<15}{path}")

    # Complexity Analysis
    print("\n========== COMPLEXITY ANALYSIS ==========")
    print("Time Complexity  : O((V + E) log V)")
    print("Space Complexity : O(V + E)")

    # Result
    print("\n========== RESULT ==========")
    print(
        "Dijkstra's algorithm successfully calculated "
        "the shortest paths from source vertex 0 "
        "to all other vertices."
    )


if __name__ == "__main__":
    main()