'''
  * 아이디어 1
    - 무게의 순위를 측정하기 위해 i -> k, k -> j 로 순위가 매겨져 있다면 i -> j 순위를 매길 수 있다.
    - 따라서 플로이드와샬 알고리즘을 사용하고,
    - 완성된 그래프의 행과 열의 합이 구분할 수 있는 개수를 의미한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for up, down in zip(graph, zip(*graph)):
    print(n-1 - (sum(up) + sum(down)))