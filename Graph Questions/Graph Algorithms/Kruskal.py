#KRUSKAL ALGORITHM 
class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n 

    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

            return True
        return False
    
def kruskal(n,edges):
    #Sorting the edges
    edges.sort()

    #Calling Constructor
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []

    #Process the Edges
    for weight,u,v in edges:
        if uf.union(u,v):
            mst_weight += weight
            mst_edges.append((u,v))

    return mst_weight,mst_edges

if __name__ == "__main__":
    # Number of vertices (0 to n-1)
    n = 4

    # List of edges: (weight, u, v)
    edges = [
        (1, 0, 1),
        (4, 0, 2),
        (3, 1, 2),
        (2, 1, 3),
        (5, 2, 3)
    ]

    mst_weight, mst_edges = kruskal(n, edges)
    print(f"Total weight of MST: {mst_weight}")
    print(f"Edges in the MST: {mst_edges}")
