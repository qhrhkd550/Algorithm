import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()


def dfs(path, begin):
    if len(path) == m:
        print(*path)
        return

    for i in range(begin, n):
        dfs(path + [data[i]], i)

dfs([], 0)