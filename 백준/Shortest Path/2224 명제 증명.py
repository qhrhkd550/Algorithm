import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque, defaultdict

n = int(input())
graph = defaultdict(list)
answer = defaultdict(list)
visit = {}
for _ in range(n):
    h = input()
    pre, post = h.split(" => ")
    graph[pre].append(post)
    answer[pre].append(post)

def bfs(start, visit):
    q = deque()
    q.append(start)
    visit[start] = True

    while q:
        now = q.popleft()
        for next in graph[now]:
            if next in visit and not visit[next]:
                visit[next] = True
                q.append(next)
                answer[now].append(next)


for g in graph:
    tmp_visit = visit.copy()
    bfs(g, tmp_visit)

print(answer)


