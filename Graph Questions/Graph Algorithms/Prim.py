import heapq

def tree(V,E,edges):
    adj = [[] for _ in range(V)]
    
    for u,v,wt in edges:
        adj[u].append((v,wt))
        adj[v].append((u,wt))

    pq = []
    visited = [False] * V 
    res = 0 
    #Sending the value of weight and u
    heapq.heappush(pq,(0,0))

    while pq:
        wt,u = heapq.heappop(pq)
        if visited[u]:
            continue
        res += wt
        visited[u] = True

        for v,weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq,(weight,v))

    return res
if __name__ == "__main__":
    graph = [[0, 1, 5],
             [1, 2, 3],
             [0, 2, 1]]
    print(tree(3, 3, graph))