#DFS Recursive
def dfs_rec(adj,visited,source):
    visited[source]=True
    print(source,end=" ")
    for i in adj[source]:
        if not visited[i]:
            dfs_rec(adj,visited,i)

#DFS
def dfs(adj,source):
    visited = [False] * len(adj)
    dfs_rec(adj,visited,source)

#Adding edges to adjacency matrix
def add_edge(adj,a,b):
    adj[a].append(b)
    adj[b].append(a)

#Main Function
v=5 #Number of vertices
adj = [[] for _ in range(v)]
edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]
for e in edges:
    add_edge(adj,e[0],e[1])

source = 1
print("Source is ",source)
dfs(adj,source)

#Implements Stack