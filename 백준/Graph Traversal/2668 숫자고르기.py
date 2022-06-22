import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
num = [0] + [int(input()) for _ in range(n)]

def dfs(i, count, path):
    if count == i:
        tmp = sum(path)
        for p in path:
            tmp -= num[p]
        if tmp == 0:
            return path
        return

    for j in range(1, n+1):
        if not visit[j]:
            visit[j] = True
            res = dfs(i, count + 1, path + [j])
            if res is not None:
                return res
            visit[j] = False

for i in range(n, 0, -1):
    visit = [False] * (n+1)
    res = dfs(i, 0, [])
    if res is not None:
        print(len(res))
        for r in res:
            print(r)
        break