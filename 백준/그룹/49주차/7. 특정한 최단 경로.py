import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

# n, e = map(int, input().split())
# data = [[float('inf')] * (n+1) for _ in range(n+1)]
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     data[a][b] = c
#     data[b][a] = c
#
# v1, v2 = map(int, input().split())
#
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i != j:
#                 data[i][j] = min(data[i][k] + data[k][j], data[i][j])
#
#
# if data[v1][v2] == float('inf') and data[v2][v1] == float('inf'):
#     print(-1)
# elif data[v1][v2] == float('inf'):
#     print(data[1][v2] + data[v2][v1] + data[v1][n])
# elif data[v2][v1] == float('inf'):
#     print(data[1][v1] + data[v1][v2] + data[v2][n])
# else:
#     print(min(data[1][v2] + data[v2][v1] + data[v1][n], data[1][v1] + data[v1][v2] + data[v2][n]))

n, e = map(int, input().split())
data = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(x):
    q = []
    distance = [float('inf')] * (n+1)
    heapq.heappush(q, (x, 0))
    distance[x] = 0

    while q:
        nx, nc = heapq.heappop(q)
        if distance[nx] < nc:
            continue

        for next, cost in data[nx]:
            if distance[next] > nc + cost:
                heapq.heappush(q, (next, nc + cost))
                distance[next] = nc + cost

    return distance

distance_1 = dijkstra(1)
distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)

answer = min(distance_1[v1] + distance_v1[v2] + distance_v2[n], distance_1[v2] + distance_v2[v1] + distance_v1[n])
if answer >= float('inf'):
    print(-1)
else:
    print(answer)