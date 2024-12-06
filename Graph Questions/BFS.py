from collections import deque

def bfs(adj,visited,source):
    q = deque()
    q.append(source)
    visited[source] = True
    while q:
        curr = q.popleft()
        print(curr,end=" ")
        for x in adj[curr]:
            if not visited[x]:
                visited[x]=True
                q.append(x)

#Adding edges to adjacency matrix
def add_edge(adj,a,b):
    adj[a].append(b)
    adj[b].append(a)

#Main Function
v=5 #Number of vertices
adj = [[] for _ in range(v)]
edges = [[0,1], [0, 2], [1, 3], [1, 4], [2, 4]]
for e in edges:
    add_edge(adj,e[0],e[1])

source = 0
visited = [False] * v
bfs(adj,visited,source)