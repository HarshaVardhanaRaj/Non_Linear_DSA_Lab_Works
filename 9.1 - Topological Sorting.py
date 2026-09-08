from collections import deque

def topological_sort(graph,n):
    
    indegree=[0]*n
    
    for v in graph:
        for w in graph[v]:
            indegree[w]+=1
    Q=deque()
    
    for v in range(n):
        if indegree[v]==0:
            Q.append(v)
            
    order=[]
    
    while Q:
        v=Q.popleft()
        order.append(v)
        for w in graph[v]:
            indegree[w]-=1
            if indegree[w]==0:
                Q.append(w)
                
    if len(order)!=n:
        return "Graph Contains a Cycle"
    return order


graph={
        0:[1,2],
        1:[3],
        2:[3],
        3:[4],
        4:[]
      }

print(topological_sort(graph,5))
