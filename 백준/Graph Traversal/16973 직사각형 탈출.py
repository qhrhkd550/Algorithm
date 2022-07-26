'''
  * 아이디어 1
    - 도형의 모든 좌표를 알고 있을 필요는 없다. 가장 왼쪽 위 좌표만 가지고 탐색한다.
    - checking_location : 도형이 범위를 벗어나는지 확인하는 함수이다. 가장왼쪽 위 좌표와 가장 오른쪽 아래 좌표만 확인한다.
    - checking_wall : 도형안에 벽이 있는지 확인하는 함수이다. 방향에 따라 필요한 면만 확인한다. 전부 확인하면 시간초과가 발생한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
h, w, sr, sc, fr, fc = map(int, input().split())

#    우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def checking_location(x, y): # 가장 왼쪽 위 좌표, 가장 오른쪽 아래 좌표만 확인
    if x < 0 or x >= n or y < 0 or y >= m:
        return True
    if x+h-1 < 0 or x+h-1 >= n or y+w-1 < 0 or y+w-1 >= m:
        return True

    return False

def checking_wall(x, y, d): # 방향에 따라 도형의 한 면만 확인
    if d == 0: # 우
        for i in range(h):
            if y+w < m and data[x+i][y+w] == 1:
                return True
        return False

    elif d == 1: # 하
        for i in range(w):
            if x+h < n and data[x+h][y+i] == 1:
                return True
        return False

    elif d == 2: # 좌
        for i in range(h):
            if y-1 >= 0 and data[x+i][y-1] == 1:
                return True
        return False

    elif d == 3: # 상
        for i in range(w):
            if x-1 >= 0 and data[x-1][y+i] == 1:
                return True
        return False


def bfs(x, y):
    q = deque()
    visit = [[0] * m for _ in range(n)]
    visit[x][y] = 1
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if x == fr-1 and y == fc-1:
            return visit[x][y] - 1

        for i in range(4): # 가장 왼쪽 위 좌표
            nx = x + dx[i]
            ny = y + dy[i]

            if checking_location(nx, ny): # 가장 왼쪽 위 좌표, 가장 오른쪽 아래 좌표만 확인
                continue

            if visit[nx][ny] != 0:
                continue

            if checking_wall(x, y, i): # 방향에 따라 도형의 한 면만 확인
                continue

            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))
result = bfs(sr-1, sc-1)

if result:
    print(result)
else:
    print(-1)