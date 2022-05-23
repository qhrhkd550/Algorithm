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
        dfs(path + [data[i]])

dfs([])