class graph:

    def __init__(self,n):
        self.n = n
        self.adj_mat = [[0]*n for _ in range(n)]

    def add_edge(self,src,dest):
        self.adj_mat[src][dest] = 1
        self.adj_mat[dest][src] = 1


    def display(self):
        for row in self.adj_mat:
            print(row)


g = graph(5)
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(3,4)
g.display()
