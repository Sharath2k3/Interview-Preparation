v = 4
INF = float('inf')


def floyd_warshall(graph):
    
    dist = [row for row in graph]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
                
    return dist

    
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]
shortest_paths = floyd_warshall(graph)

for x in shortest_paths:
    print(x)


