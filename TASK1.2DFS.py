graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in graph[node]:
            dfs(neighbour)

start = input("Enter starting node: ")
print("DFS Traversal:")
dfs(start)



// OUTPUT
Enter starting node: A
DFS Traversal:
A B D E C F G 
