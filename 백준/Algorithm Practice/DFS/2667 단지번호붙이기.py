import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = [list(map(int, input())) for _ in range(n)]
#    우  하  좌  상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, count):
    visit[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if visit[nx][ny] or not data[nx][ny]:
            continue

        count = dfs(nx, ny, count + 1)

    return count

visit = [[False] * n for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1 and not visit[i][j]:
            answer.append(dfs(i, j, 1))

answer.sort()
print(len(answer))
for a in answer:
    print(a)