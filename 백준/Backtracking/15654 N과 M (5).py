import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def dfs(path):
    if len(path) == m:
        print(*path)
        return

    for i in range(n):
        if not visit[data[i]]:
            visit[data[i]] = True
            dfs(path + [data[i]])
            visit[data[i]] = False

visit = [False] * (max(data) + 1)
dfs([])