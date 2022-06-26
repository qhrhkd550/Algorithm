'''
  * 아이디어 1
    - 모든지점에서 최단거리를 구하는 플로이드와샬 알고리즘은 시간초과
    - 따라서 다익스트라 사용
    - 단, 다익스트라도 친구집 위치를 제외한 모든 지점에서 수행하는 것은 시간초과
    - 따라서 a, b, c 친구의 집에서 다익스트라를 적용한다.
    - 친구의 집이 아닌 각 위치(i)에서 친구집까지 거리의 최대값은 a,b,c 위치에서 i까지 거리의 최소값과 같다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

n = int(input())
a, b, c = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d, e, cost = map(int, input().split())
    graph[d].append((e, cost))
    graph[e].append((d, cost))

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

answer_value = 0
answer_node = 0
dist_a = Dijkstra(a)
dist_b = Dijkstra(b)
dist_c = Dijkstra(c)


for i in range(1, n+1):
    if answer_value < min(dist_a[i], dist_b[i], dist_c[i]):
        answer_value = min(dist_a[i], dist_b[i], dist_c[i])
        answer_node = i

print(answer_node)
