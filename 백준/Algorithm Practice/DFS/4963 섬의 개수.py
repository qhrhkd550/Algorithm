import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10000)
dx = [0, 1, 0, -1, -1, 1, 1, -1]
dy = [1, 0, -1, 0, 1, 1, -1, -1]

def dfs(x, y):
    visit[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if visit[nx][ny] or not data[nx][ny]:
            continue

        dfs(nx, ny)


while True:
    count = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    data = [list(map(int, input().split())) for _ in range(h)]
    visit = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if data[i][j] == 1 and not visit[i][j]:
                dfs(i, j)
                count += 1

    print(count)