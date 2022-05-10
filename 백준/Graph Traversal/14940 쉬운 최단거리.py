'''
  * 아이디어 1
    - 목표지점까지 거리가 0인경우,
    - 원래 갈 수 없는 땅인 경우
    - 원래 갈 수 있지만 도달할 수 없는 경우
    - 위 3가지 경우를 잘 구분하면 되는 문제이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

def find_target():
    for i in range(n):
        for j in range(m):
            if data[i][j] == 2:
                return (i, j)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visit[nx][ny] != -1 or data[nx][ny] == 0:
                continue

            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))



visit = [[-1] * m for _ in range(n)]
x, y = find_target()
bfs(x, y)
for i in range(n):
    for j in range(m):
        if visit[i][j] == -1 and data[i][j] == 1: # 갈 수 있지만 도달하지 못한 경우
            print(-1, end=' ')
        elif visit[i][j] == -1 and data[i][j] == 0: # 원래 못가는 경우
            print(0, end=' ')
        else: # 나머지 경우
            print(visit[i][j], end=' ')
    print()