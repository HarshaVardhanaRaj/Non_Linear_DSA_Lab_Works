#BFS

graph1 = {
          'A': ['B', 'C'],
          'B': ['D', 'E'],
          'C': ['F'],
          'D': [],
          'E': [],
          'F':[]
         }

visited = []
queue = []

def bfs(visited, graph, start_vertex):
    visited.append(start_vertex)
    queue.append(start_vertex)

    print("Result: ", end=" ")

    while queue:
        s = queue.pop(0)
        print (s, end=" ")
            
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


start_vertex = input("Enter the starting node: ")
bfs(visited, graph1, start_vertex)                                    

