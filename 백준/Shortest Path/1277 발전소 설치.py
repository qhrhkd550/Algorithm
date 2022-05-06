'''
  * 아이디어 1
    - 1부터 n까지의 최단거리를 구해야 하므로, 플로이드와샬보다는 다익스트라르 사용하는 것이 시간초과가 발생하지 않는다.
    - 좌표계에 발전소가 있기 때문에 노드들 간의 거리는 유클리디안 거리를 사용해서 구할 수 있다. 단, 거리가 m을 넘지 않는 것만 그래프에 추가한다.
    - 결과에 기존에 남아있는 엣지 값을 포함하면 안되므로, 기존에 연결정보가 남아있는 것은 거리를 0으로 계산한다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
import math, heapq
from collections import defaultdict

n, w = map(int, input().split())
m = float(input())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
point = defaultdict()

index = 1
for _ in range(n): # 그래프를 구성하기 위해 좌표를 입력받고, index로 관리한다.
    x, y = map(int, input().split())
    point[index] = (x, y)
    index += 1

graph = [[] for _ in range(n+1)]
for _ in range(w): # 남아있는 w들에 대해 거리를 0으로 계산한다.
    v1, v2 = map(int, input().split())
    graph[v1].append((0, v2))
    graph[v2].append((0, v1))

for i in range(1, n+1): # 모든 노드들 간의 거리 정보를 추가하는데 거리가 m보다 작은 값을 가지는 것만 그래프에 추가한다.
    for j in range(1, n+1):
        if i != j:
            distance = math.sqrt((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2)
            if distance < m:
                graph[i].append((distance, j))

def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue

        for c, next in graph[now]:
            if cost + c < dist[next]:
                dist[next] = cost + c
                heapq.heappush(q, (cost+c, next))

dist = [float('inf')] * (n+1)
Dijkstra(1)
print(int(dist[n] * 1000))