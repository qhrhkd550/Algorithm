import sys
input = lambda : sys.stdin.readline().rstrip()

m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if data[nx][ny] >= data[x][y]:
            continue

        ways += dfs(nx, ny)

    dp[x][y] = ways
    return dp[x][y]

dp = [[-1] * n for _ in range(m)]
print(dfs(0, 0))