import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

def dfs(begin, path):
    if len(path) == m:
        print(*path)
        return

    for i in range(begin, n+1):
        if not visit[i]:
            visit[i] = True
            dfs(i+1, path+[i])
            visit[i] = False

visit = [False] * (n+1)
dfs(1, [])