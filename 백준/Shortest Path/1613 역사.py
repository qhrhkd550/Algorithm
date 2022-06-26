import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for _ in range(k):
    pre, post = map(int, input().split())
    graph[pre-1][post-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

s = int(input())
for _ in range(s):
    x, y = map(int, input().split())
    if graph[x-1][y-1] == 1:
        print(-1)
    elif graph[y-1][x-1] == 1:
        print(1)
    else:
        print(0)