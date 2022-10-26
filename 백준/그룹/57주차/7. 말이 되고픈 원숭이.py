import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

k = int(input())
w, h = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(h)]

dx = [0, 1, 0, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 0, -1, 0, 1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    visit[x][y][z] = 0

    while q:
        x, y, z = q.popleft()

        if x == h-1 and y == w-1:
            print(visit[x][y][z])
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if visit[nx][ny][z] != -1 or data[nx][ny] == 1:
                continue

            visit[nx][ny][z] = visit[x][y][z] + 1
            q.append((nx, ny, z))

        if k > z:
            for i in range(4, 12):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue

                if visit[nx][ny][z+1] != -1 or data[nx][ny] == 1:
                    continue

                visit[nx][ny][z+1] = visit[x][y][z] + 1
                q.append((nx, ny, z+1))

    print(-1)

visit = [[[-1] * (k+1) for _ in range(w)] for _ in range(h)]
bfs(0, 0, 0)
