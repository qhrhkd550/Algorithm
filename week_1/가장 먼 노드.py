'''
* 문제 유형 : 그래프

* 체감난이도 : **

* 아이디어 1
  - 다익스트라 알고리즘을 통해 1번 노드부터 다른 모든 노드들까지의 거리를 계산
'''

import heapq

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    cost = [int(1e9)] * (n+1)
    
    def Dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        cost[start] = 0
        
        while q:
            c, node = heapq.heappop(q)
            if cost[node] < c:
                continue
                
            for g in graph[node]:
                if cost[g] > c + 1:
                    cost[g] = c + 1
                    heapq.heappush(q, (c+1, g))
        
    Dijkstra(1)
    return cost[1:].count(max(cost[1:]))
