import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny] != 0 or data[nx][ny] == 0:
                continue

            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))

visit = [[0] * m for _ in range(n)]
bfs(0, 0)
print(visit[n-1][m-1])