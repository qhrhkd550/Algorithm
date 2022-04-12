'''
* 아이디어 1
  - visit를 True False로 하지말고, 부모 노드의 번호로 가져가면 편하다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = start

    while q:
        x = q.popleft()

        for next in graph[x]:
            if visit[next] == -1:
                visit[next] = x
                q.append(next)

visit = [-1] * (n+1)
bfs(1)
for v in visit[2:]:
    print(v)