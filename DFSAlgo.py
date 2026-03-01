graph = {
    'A':['B' , 'C' , 'D'],
    'B':['E' , 'F'],
    'C':['G' , 'H'],
    'D':['I'],
    'E':['J'],
    'F':[],
    'G':['K'],
    'H':[],
    'I':[],
    'J':[],
    'K':['L'],
    'L':[]
}

def dfs(graph,node,visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node,end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph,neighbour,visited)

dfs(graph,'A')