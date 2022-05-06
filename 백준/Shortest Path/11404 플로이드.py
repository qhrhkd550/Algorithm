'''
  * 아이디어 1
    - 단순히 플로이드 와샬을 사용하는 문제이다.
    - A, B를 연결하는 엣지가 하나가 아니라 여려개일 수 있기 때문에, 최소값을 넣어야 한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] != float('inf'):
        if graph[a][b] > c:
            graph[a][b] = c
    else:
        graph[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == float('inf'):
            print(0, end= ' ')
        else:
            print(graph[i][j], end=' ')
    print()