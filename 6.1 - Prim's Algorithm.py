import heapq

def prim(graph):
    visited = set()
    min_heap = [(0, 1, None)]

    mst = []
    total_weight = 0

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if current in visited:
            continue

        visited.add(current)

        if parent is not None:
            mst.append((parent, current, weight))                            
            total_weight += weight

        for neighbor, w in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, current))

    return mst, total_weight

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
    
