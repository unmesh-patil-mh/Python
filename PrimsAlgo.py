import sys

def main():
    try:
        n = int(input("Enter number of vertices: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if n <= 0:
        print("Number of vertices must be positive.")
        return

    graph = []
    print(f"Enter adjacency matrix ({n} values per row, 0 for no edge):")

    # Input validation for adjacency matrix
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").split()))
                if len(row) != n:
                    print(f"Error: Please enter exactly {n} values.")
                else:
                    graph.append(row)
                    break
            except ValueError:
                print("Error: Please enter only integers.")

    parent = [-1] * n
    key = [sys.maxsize] * n
    mstSet = [False] * n

    key[0] = 0  # Start from first vertex

    for _ in range(n):
        minimum = sys.maxsize
        u = -1

        # Find vertex with minimum key value
        for v in range(n):
            if not mstSet[v] and key[v] < minimum:
                minimum = key[v]
                u = v

        # If no vertex found (disconnected graph)
        if u == -1:
            break

        mstSet[u] = True

        # Update adjacent vertices
        for v in range(n):
            if (
                graph[u][v] != 0
                and not mstSet[v]
                and graph[u][v] < key[v]
            ):
                parent[v] = u
                key[v] = graph[u][v]

    print("\nEdge \tWeight")
    total_weight = 0

    for i in range(1, n):
        if parent[i] != -1:
            print(f"{parent[i]} - {i}\t{graph[i][parent[i]]}")
            total_weight += graph[i][parent[i]]
        else:
            print(f"{i} is disconnected.")

    print(f"\nTotal weight of MST: {total_weight}")


if __name__ == "__main__":
    main()