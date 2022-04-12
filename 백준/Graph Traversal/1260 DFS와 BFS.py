import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()

def dfs(v):
    print(v, end=' ')
    for next in graph[v]:
        if not visit[next]:
            visit[next] = True
            dfs(next)

visit = [False] * (n+1)
visit[v] = True
dfs(v)
print()

def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = True

    while q:
        x = q.popleft()
        print(x, end=' ')
        for next in graph[x]:
            if not visit[next]:
                visit[next] = True
                q.append(next)

visit = [False] * (n+1)
bfs(v)
