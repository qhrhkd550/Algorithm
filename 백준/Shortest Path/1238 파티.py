'''
  * 아이디어 1
    - 플로이드와샬은 시간초과 발생
    - 다익스트라를 사용해서 모든 노드에서 최단거리를 구한 후,
    - i -> x -> i 의 최단거리의 최대값을 구한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def Dijkstra(start):
    q = []
    distance = [float('inf')] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue

        for next, dist in graph[node]:
            if cost + dist < distance[next]:
                distance[next] = cost + dist
                heapq.heappush(q, (cost+dist, next))

    return distance

answer = 0
dist_all_node = [[float('inf') for _ in range(n)]]
for i in range(1, n+1):
    dist_all_node.append(Dijkstra(i))

for i in range(1, n+1):
    if answer < dist_all_node[i][x] + dist_all_node[x][i]:
        answer = dist_all_node[i][x] + dist_all_node[x][i]

print(answer)