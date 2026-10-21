def tsp(cost):
    n=len(cost)
    visited=[False]*n
    visited[0]=True
    best_cost=float('inf')
    best_path=[]

    def branch(city,count,current_cost,path):
        nonlocal best_cost,best_path

        if count==n:
            total_cost=current_cost+cost[city][0]
            if total_cost<best_cost:
                best_cost=total_cost
                best_path=path+[0]
            return

        for next_city in range(n):
            if not visited[next_city]:
                new_cost=current_cost+cost[city][next_city]
                if new_cost<best_cost:
                    visited[next_city]=True
                    branch(
                        next_city,
                        count+1,
                        new_cost,
                        path+[next_city]
                        )
                    visited[next_city]=False
    branch(0,1,0,[0])
    return best_cost,best_path

cost=[
      [0,10,15,20],
      [10,0,35,25],
      [15,35,0,30],
      [20,25,30,0]
     ]

minimum_cost, path = tsp(cost)
print("Minimum Cost = ", minimum_cost)
print("Optimal Tour = ", end=" ")

for city in path:
    print(city+1, end=" ")
