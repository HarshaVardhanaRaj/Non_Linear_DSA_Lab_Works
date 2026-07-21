#DFS

graph1 = {
          'A': ['B', 'C'],
          'B': ['D', 'E'],
          'C': ['F'],
          'D': [],
          'E': [],
          'F':[]
         }

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
            
    for neighbour in graph[node]:
        dfs(visited, graph, neighbour)

start_vertex = input("Enter the starting node: ")
dfs(visited, graph1, start_vertex)                                    

