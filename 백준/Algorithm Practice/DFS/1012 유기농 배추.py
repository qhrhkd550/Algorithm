import sys
input = lambda : sys.stdin.readline().rstrip()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    visit[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if visit[nx][ny] or not data[nx][ny]:
            continue

        dfs(nx, ny)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        data[x][y] = 1

    visit = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] and not visit[i][j]:
                dfs(i, j)
                count += 1

    print(count)