'''
* 아이디어 1
  - 순열 문제이다.
  - itertools를 써도 상관없다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

def dfs(path):
    if len(path) == m:
        print(*path)
        return

    for i in range(1, n+1):
        if not visit[i]:
            visit[i] = True
            dfs(path + [i])
            visit[i] = False

visit = [False] * (n+1)
dfs([])