graph = {
    5: [2, 6],
    6: [3, 8],
    2: [1],
    8: [0, 7],
    1: [],
    0:[],
    7:[],
    3:[]
}

visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        node = queue.pop(0)
        print(node,end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS Traversal is: ")
bfs(visited,graph,5)