import sys
from collections import deque, defaultdict
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
ladder_info = defaultdict(int)
for _ in range(n):
    x, y = map(int, input().split())
    ladder_info[x] = y

snake_info = defaultdict(int)
for _ in range(m):
    u, v = map(int, input().split())
    snake_info[u] = v

def bfs(x):
    q = deque()
    q.append(x)

    visit = [float('inf')] * 101
    visit[x] = 0

    while q:
        x = q.popleft()
        if x == 100:
            return visit[x]

        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue

            if visit[nx] != float('inf'):
                continue

            if nx in ladder_info.keys():
                q.append(ladder_info[nx])
                visit[ladder_info[nx]] = min(visit[ladder_info[nx]], visit[x] + 1)

            elif nx in snake_info.keys():
                q.append(snake_info[nx])
                visit[snake_info[nx]] = min(visit[snake_info[nx]], visit[x] + 1)

            else:
                q.append(nx)
                visit[nx] = min(visit[nx], visit[x] + 1)

answer = bfs(1)
print(answer)