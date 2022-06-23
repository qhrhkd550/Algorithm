'''
  * 아이디어 1
    - 조건을 만족하기 위해서는 dfs의 깊이가 4가되면 조건을 만족한다.
    - 따라서 깊이가 4일때 return True를 해준다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(depth, now):
    if depth == 4:
        return True

    for next in graph[now]:
        if not visit[next]:
            visit[next] = True
            res = dfs(depth + 1, next)
            if res:
                return res
            visit[next] = False


visit = [False] * n
for i in range(n):
    visit[i] = True
    res = dfs(0, i)
    if res:
        print(1)
        break
    visit[i] = False

if not res:
    print(0)