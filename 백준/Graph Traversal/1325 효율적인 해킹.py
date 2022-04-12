'''
* 아이디어 1
  - 모든 노드를 시작점으로 bfs를 통해 방문할 수 있는 노드들의 수를 구하면 된다.
  - 매번 bfs를 수행할 때마다 최대값을 저장시키고, 모든 결과를 answer에 저장시킨다.
  - 저장된 answer에서 최대값과 같은 번호만 출력시킨다.

* 아이디어 2
  - dfs로 구현하였지만, 항상 메모리초과가 발생한다... 이유는 모르겠다... setrecursionlimit를 10000으로 풀어도 메모리초과가 발생한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

def bfs(start):
    q = deque()
    q.append(start)
    count = 0
    visit[start] = True

    while q:
        x = q.popleft()

        for next in graph[x]:
            if not visit[next]:
                visit[next] = True
                q.append(next)
                count += 1

    return count

# sys.setrecursionlimit(10006)
# def dfs(start, count):
#     visit[start] = True
#     for next in graph[start]:
#         if not visit[next]:
#             count = dfs(next, count + 1)
#
#     return count

answer = []
max_value = 0
for i in range(1, n+1):
    visit = [False] * (n+1)
    count = bfs(i)
    # count = dfs(i, 0)
    if max_value < count:
        max_value = count
    answer.append([i, count])

for x, y in answer:
    if max_value == y:
        print(x, end = ' ')