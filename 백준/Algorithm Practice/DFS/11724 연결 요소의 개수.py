import sys
input = lambda : sys.stdin.readline().rstrip()

def dfs(now):
    visit[now] = True

    for next in graph[now]:
        if not visit[next]:
            visit[next] = True
            dfs(next)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (n+1)
answer = 0
for i in range(1, n+1):
    if not visit[i]:
        dfs(i)
        answer += 1

print(answer)