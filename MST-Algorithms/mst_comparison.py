import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True


# Kruskal's Algorithm
def kruskal(n, edges):
    edges.sort()

    uf = UnionFind(n)
    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == n - 1:
                break

    return mst, total_cost


# Prim's Algorithm
def prim(n, graph, start=0):
    key = [float("inf")] * n
    parent = [-1] * n
    in_mst = [False] * n

    key[start] = 0
    priority_queue = [(0, start)]

    mst = []
    total_cost = 0

    while priority_queue:
        weight, u = heapq.heappop(priority_queue)

        if in_mst[u]:
            continue

        in_mst[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, weight))
            total_cost += weight

        for v, edge_weight in graph.get(u, []):
            if not in_mst[v] and edge_weight < key[v]:
                key[v] = edge_weight
                parent[v] = u
                heapq.heappush(priority_queue, (edge_weight, v))

    return mst, total_cost


def main():
    # Input Graph
    n = 7

    edges = [
        (7, 0, 1),
        (5, 0, 3),
        (8, 1, 2),
        (9, 1, 3),
        (7, 1, 4),
        (5, 2, 4),
        (15, 3, 4),
        (6, 3, 5),
        (8, 4, 5),
        (9, 4, 6),
        (11, 5, 6),
    ]

    graph = {}

    for weight, u, v in edges:
        graph.setdefault(u, []).append((v, weight))
        graph.setdefault(v, []).append((u, weight))

    # Run Algorithms
    kruskal_mst, kruskal_cost = kruskal(n, edges.copy())
    prim_mst, prim_cost = prim(n, graph)

    # Display Input
    print("========== INPUT GRAPH ==========")
    print(f"Number of Vertices : {n}")
    print("\nEdges (Source, Destination, Weight):")

    for weight, u, v in edges:
        print(f"({u}, {v}) --> Weight = {weight}")

    # Kruskal Output
    print("\n========== KRUSKAL'S ALGORITHM ==========")
    print("Minimum Spanning Tree:")

    for u, v, weight in kruskal_mst:
        print(f"Edge ({u}, {v}) --> Weight = {weight}")

    print(f"\nTotal Cost of MST : {kruskal_cost}")

    # Prim Output
    print("\n========== PRIM'S ALGORITHM ==========")
    print("Minimum Spanning Tree:")

    for u, v, weight in prim_mst:
        print(f"Edge ({u}, {v}) --> Weight = {weight}")

    print(f"\nTotal Cost of MST : {prim_cost}")

    # Comparison
    print("\n========== COMPARISON ==========")

    if prim_cost == kruskal_cost:
        print("Result : Both algorithms produced the same Minimum Spanning Tree cost.")
    else:
        print("Result : The algorithms produced different Minimum Spanning Tree costs.")

    print(f"\nKruskal's MST Cost : {kruskal_cost}")
    print(f"Prim's MST Cost    : {prim_cost}")

    # Complexity Analysis
    print("\n========== COMPLEXITY ANALYSIS ==========")
    print("Kruskal's Algorithm")
    print("Time Complexity  : O(E log E)")
    print("Space Complexity : O(V)")

    print("\nPrim's Algorithm (using Priority Queue)")
    print("Time Complexity  : O(E log V)")
    print("Space Complexity : O(V + E)")


if __name__ == "__main__":
    main()