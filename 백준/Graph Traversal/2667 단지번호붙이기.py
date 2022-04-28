import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
data = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny] != 0 or data[nx][ny] == 0:
                continue

            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))
            count += 1

    return count

answer = []
visit = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if data[i][j] == 1 and visit[i][j] == 0:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for a in answer:
    print(a)