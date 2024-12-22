def topologicalsortutil(v,adj,visited,stack):
    visited[v] = True

    for i in adj[v]:
        if not visited[i]:
            topologicalsortutil(i,adj,visited,stack)
    
    stack.append(v)

def topological_sort(adj,v):
    stack = []
    visited = [False] * v 

    for i in range(v):
        if not visited[i]:
            topologicalsortutil(i,adj,visited,stack)

    print("Topological Sort : ",end=" ")

    while stack:
        print(stack.pop(),end=" ")

if __name__ == "__main__":
    v = 4

    edges = [[0, 1], [1, 2], [3, 1], [3, 2]]

    adj = [[] for _ in range(v)]

    for i in edges:
        adj[i[0]].append(i[1])

    topological_sort(adj,v)