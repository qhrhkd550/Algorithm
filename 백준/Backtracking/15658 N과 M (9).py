import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
answer = []


def dfs(path):
    if len(path) == m:
        answer.append(tuple(path))
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            dfs(path + [data[i]])
            visit[i] = False


visit = [False] * n
dfs([])
answer = list(set(answer))
answer = sorted(answer)
for a in answer:
    print(*a)