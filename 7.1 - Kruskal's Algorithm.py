class DisjointSet:

    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 != root2:
            self.parent[root2] = root1


def kruskal(vertices, edges):
    
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(vertices)

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost



vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


edges2 = [
            ('A', 'B', 4),
            ('A', 'H', 8),
            ('B', 'H', 11),
            ('B', 'C', 8),
            ('C', 'D', 7),
            ('C', 'F', 4),
            ('C', 'I', 2),
            ('D', 'F', 14),
            ('D', 'E', 9),
            ('E', 'F', 10),
            ('F', 'G', 2),
            ('G', 'H', 1),
            ('H', 'I', 7),
            ('I', 'G', 6)
        ]

mst, cost = kruskal(vertices, edges2)

print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")

print("Total Cost:", cost)
