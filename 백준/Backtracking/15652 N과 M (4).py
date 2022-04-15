'''
* 아이디어 1
  - 중복 조합 문제이다.
  - 조합 문제에서 방문에 대한 개념을 없앤다.
  - 또한, 중복을 위해 dfs에 i+1이 아닌 i를 begin값으로 넣어준다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

def dfs(begin, path):
    if len(path) == m:
        print(*path)
        return

    for i in range(begin, n+1):
        dfs(i, path + [i])

dfs(1, [])

