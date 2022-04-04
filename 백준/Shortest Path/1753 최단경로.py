'''
* 체감 난이도 : **

* 아이디어 1
  - 출발점이 고정되어 있으므로 다익스트라 알고리즘을 통해 출발점에서 다른 모든 지점까지 거리를 구한다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

import heapq

V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

distance = [int(1e9)] * (V+1)

def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue
        for dist, next in graph[node]:
            if cost + dist < distance[next]:
                distance[next] = cost + dist
                heapq.heappush(q, (cost+dist, next))

Dijkstra(k)
for i in range(1, V+1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
