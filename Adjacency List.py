class graph:

    def __init__(self,n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]

    def add_edge(self,src,dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)


    def display(self):
        for i in range (self.n):
            print("Adjacency List of Vertex {}".format(i), end=" ")
            for j in self.adj_list[i]:
                print("-> {}".format(j), end=" ")
            print()


g = graph(5)
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(3,4)
g.display()


        
