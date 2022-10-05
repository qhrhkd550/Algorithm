import sys
input = lambda : sys.stdin.readline().rstrip()

computer = int(input())
n = int(input())
graph = [[] for _ in range(computer+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
def dfs(now):
    global count
    visit[now] = True
    for next in graph[now]:
        if not visit[next]:
            dfs(next)
            count += 1

visit = [False] * (computer + 1)
dfs(1)
print(count)
