INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    
    # Create distance matrix
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]

    # Update distances using intermediate vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Example graph (adjacency matrix)
graph = [
    [0,   3,   INF, 5],
    [2,   0,   INF, 4],
    [INF, 1,   0,   INF],
    [INF, INF, 2,   0]
]

result = floyd_warshall(graph)

print("Shortest distance matrix:")
for row in result:
    print(row)
