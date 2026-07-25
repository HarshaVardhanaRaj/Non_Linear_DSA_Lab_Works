# Dijkstra's Algorithm

import heapq

def shortest_path(graph, s):
    dist = {v: float('inf') for v in graph}
    dist[s] = 0

    Q = [(0, s)]
    visited = set()

    while Q:
        current_distance, u = heapq.heappop(Q)

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u]:
            if v not in visited:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(Q, (dist[v],v))

    return dist


graph = {
          'a': [('b', 2)],
          'b': [('c', 1)],
          'c': [('d', 1)],
          'd': [('a', 2)]
        }

source = 'a'

distances = shortest_path(graph, source)

for v in distances:
    print(f"Shortest Distance from {source} to {v} = {distances[v]}")
