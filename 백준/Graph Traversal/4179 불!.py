import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

r, c = map(int, input().split())
data = [list(map(str, input())) for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def spread_fire():
    while fire_q:
        qlen = len(fire_q)
        while qlen:
            x, y = fire_q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if data[nx][ny] == '#' or data[nx][ny] == 'F':
                    continue

                if fire[nx][ny] > 0:
                    continue

                fire[nx][ny] = fire[x][y] + 1
                fire_q.append((nx, ny))
            qlen -= 1
#
def move():
    while j_q:
        qlen = len(j_q)
        while qlen:
            x, y = j_q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    return ji[x][y] + 1

                if data[nx][ny] == '#':
                    continue

                if ji[nx][ny] > 0:
                    continue

                if fire[nx][ny] > 0 and fire[nx][ny] <= ji[x][y] + 1:
                    continue

                ji[nx][ny] = ji[x][y] + 1
                j_q.append((nx, ny))
            qlen -= 1

    return "IMPOSSIBLE"

j_q = deque()
fire_q = deque()
fire = [[0] * c for _ in range(r)]
ji = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if data[i][j] == 'J':
            j_q.append((i, j))
        elif data[i][j] == 'F':
            fire_q.append((i, j))

spread_fire()
print(move())