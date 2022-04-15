'''
* 아이디어 1
  - 중복 순열 문제이다.
  - 순열 문제에서 방문에 대한 개념을 없애면 중복 순열이 된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

def dfs(path):
    if len(path) == m:
        print(*path)
        return

    for i in range(1, n+1):
        dfs(path + [i])

dfs([])
