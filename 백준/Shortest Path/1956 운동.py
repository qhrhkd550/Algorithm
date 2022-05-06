'''
  * 아이디어 1
    - 플로이드 와샬을 수행할 때, 일반적으로 자기자신은 0으로 초기화한다.
    - 하지만 graph[i][i]를 무한대로 설정하고 플로이드와샬을 수행했을 경우,
    - 대각선 정보는 각 노드로의 사이클 길이가 된다. 꼭 외우자.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

v, e = map(int, input().split())
graph = [[float('inf')] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c


for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer = float('inf')
for i in range(1, v+1):
    answer = min(answer, graph[i][i])

if answer == float('inf'):
    print(-1)
else:
    print(answer)