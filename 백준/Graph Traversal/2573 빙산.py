import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def count_empty(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
            
        if data[nx][ny] == 0:
            if data[x][y] > water[x][y]:
                water[x][y] += 1

def melt():
    for i in range(n):
        for j in range(m):
            if data[i][j] > 0:
                data[i][j] -= water[i][j]

def count_sector():
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] > 0 and not visit[i][j]:
                bfs(i, j)
                count += 1
                if count == 2:
                    return True
    return False

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visit[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and data[nx][ny] > 0:
                visit[nx][ny] = True
                q.append([nx,ny])



def go():
    for i in range(n):
        for j in range(m):
            if data[i][j] > 0:
                return True
    return False

year = 0
while True:
    water = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] > 0:
                count_empty(i,j)

    # melt
    melt()

    year += 1

    if go():
        visit = [[False] * m for _ in range(n)]
        if count_sector():
            print(year)
            break
    else:
        print(0)
        break