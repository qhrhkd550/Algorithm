'''
* 아이디어 1
  - dfs와 bfs 두 가지 방법 모두 사용할 수 있다.
  - dfs인 경우, 시작점을 방문처리하고 dfs를 수행한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    answer = 0
    q = deque()
    q.append(start)
    visit[start] = True

    while q:
        x = q.popleft()
        for next in graph[x]:
            if not visit[next]:
                answer += 1
                q.append(next)
                visit[next] = True

    return answer

visit = [False] * (n+1)
print(bfs(1))


# def dfs(start, count):
#     for next in graph[start]:
#         if not visit[next]:
#             visit[next] = True
#             count = dfs(next, count + 1)
#
#     return count
#
# visit = [False] * (n+1)
# visit[1] = True
# print(dfs(1, 0))