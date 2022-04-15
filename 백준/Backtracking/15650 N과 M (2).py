'''
* 아이디어 1
  - 조합 문제이다.
  - itertools를 써도 상관없다.
  - dfs의 for문에 begin부터 시작해야 전 노드를 안보기 때문에 조합이 가능하다.
  - 만약 begin을 항상 1로 한다면 순열이 된다.
'''
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
            dfs(i+1, path + [i])
            visit[i] = False

visit = [False] * (n+1)
dfs(1, [])
