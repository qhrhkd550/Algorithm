'''
  * 아이디어 1
    - 플로이드 와샬 알고리즘을 사용한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
answer = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s][e] = c
    graph[e][s] = c

    answer[s][e] = e # s출발 e도착이면 s기준으로 e가 도착지점이 되어야 한다.
    answer[e][s] = s

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
            answer[i][j] = -1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                answer[i][j] = answer[i][k] # 먼저 들러야 하는 answer[i][k]로 값을 바꾼다.

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if answer[i][j] == -1:
            print('-', end=' ')
        else:
            print(answer[i][j], end=' ')
    print()