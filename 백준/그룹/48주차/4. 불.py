import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 0


def bfs(fire, sang):
    while sang:
        qlen = len(fire)
        while qlen:
            x, y = fire.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if data[nx][ny] == '#':
                    continue
                if data[nx][ny] == '*':
                    continue

                data[nx][ny] = '*'
                fire.append((nx, ny))
            qlen -= 1

        qlen = len(sang)
        while qlen:
            x, y = sang.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return visit[x][y] + 1

                if data[nx][ny] == '#':
                    continue

                if data[nx][ny] == "*":
                    continue

                if visit[nx][ny] > 0:
                    continue

                visit[nx][ny] = visit[x][y] + 1
                sang.append((nx, ny))

            qlen -= 1

    return "IMPOSSIBLE"


for _ in range(t):
    w, h = map(int, input().split())
    data = [list(map(str, input())) for _ in range(h)]

    sang = deque()
    fire_loc = deque()
    for i in range(h):
        for j in range(w):
            if data[i][j] == '@':
                sang.append((i, j))
            elif data[i][j] == '*':
                fire_loc.append((i, j))

    visit = [[0] * w for _ in range(h)]

    print(bfs(fire_loc, sang))
