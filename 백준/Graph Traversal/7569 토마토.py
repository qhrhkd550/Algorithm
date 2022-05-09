'''
  * 아이디어 1
    - BFS를 통해 4방향 + 아래 + 위를 살펴보면 되는 문제이다.
    - 이유는 모르겠지만, visit를 사용할 경우 정답처리가 되지 않는다.
    - data자체에서 해결가능한 경우 visit를 쓰지말자.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

m, n, h = map(int, input().split())
data = []
for _ in range(h):
    data.append([list(map(int, input().split())) for _ in range(n)])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dk = [-1, 1]

def bfs():
    time = -1
    while q:
        qlen = len(q)
        while qlen:
            k, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if data[k][nx][ny] != 0:
                    continue

                q.append((k, nx, ny))
                data[k][nx][ny] = 1
            for i in range(2):
                nk = k + dk[i]
                if nk < 0 or nk >= h:
                    continue
                if data[nk][x][y] != 0:
                    continue
                q.append((nk, x, y))
                data[nk][x][y] = 1

            qlen -= 1

        time += 1

    for k in range(h):
        for i in range(n):
            for j in range(m):
                if data[k][i][j] == 0:
                    return -1

    return time

q = deque()

zero = False
for k in range(h):
    for i in range(n):
        for j in range(m):
            if data[k][i][j] == 1:
                q.append((k, i, j))
            elif data[k][i][j] == 0:
                zero = True

if not zero:
    print(0)
else:
    result = bfs()
    print(result)

