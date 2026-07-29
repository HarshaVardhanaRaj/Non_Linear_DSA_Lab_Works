import heapq

def prim(graph):
    #initialisations
    visited = set()    #contains the visited nodes as a set
    min_heap = [(0, 1, None)]    #contains the node's (weight, name, parent) for current nodes
    mst = []    #is the minimum search tree
    total_weight = 0    #is the total cost

    while min_heap:    #when min_heap is not empty... ie. when there are nodes to be visited
        weight, current, parent = heapq.heappop(min_heap)    #weight, name and parent of current node is taken

        if current in visited:    #is current node was already visited
            continue    #it skips the iteration

        #if current node was not visited
        visited.add(current)

        if parent is not None:    #is current node is not the start node
            mst.append((parent, current, weight))    #add the weighted edge for the current node, from its parent
            total_weight += weight    #increment the total weight

        for neighbor, w in graph[current]:    #while the current node has got neighbours with weighted edge connection
            if neighbor not in visited:    #if neighbour is not already visited
                heapq.heappush(min_heap, (w, neighbor, current))    #add the details of the neighbour to min_heap

    return mst, total_weight    #return the mst and total weight

graph = {
         0: [(1, 2), (3, 6)],
         1: [(0, 2), (2, 3), (3, 8), (4,5)],
         2: [(1, 3), (4, 7)],
         3: [(0, 6), (1, 8), (4, 9)],
         4: [(1, 5), (2, 7), (3, 9)]
        }

mst, cost = prim(graph)

print("Edges in the Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} -- {v} : {w}")

print("\nTotal Cost =", cost)
    
