'''
  * 아이디어 1
    - 벽을 한 번 뚫고 지나갈 수 있으므로, visit의 각 자리는 [0, 0]으로 초기화하고, 왼쪽은 벽을 부수지 않은경우, 오른쪽은 벽을 부순 경우를 의미한다.
    - 벽을 부수지 않았을 때는 z = 0으로 두어 visit[nx][ny][z] 자리에 업데이트 해나간다.
    - 1) 탐색 중, 벽이 아니고 방문하지 않았다면 visit[nx][ny][z] = visit[x][y][z] + 1을 하면 된다.
    - 2) 탐색 중, z = 0 (아직 벽을 부순적이 없고), 방문할 곳이 벽이고 방문한적이 없다면 visit[nx][ny][z+1] = visit[x][y][z] + 1을 수행하고, q에 (nx, ny, z+1)을 넣는다.
    - q에 z+1이 들어간 순간부터 2) 케이스는 고려하지 않게 된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, z):
    q = deque()
    visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visit[x][y][0] = 1
    q.append((x, y, z))

    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if data[nx][ny] == 0 and visit[nx][ny][z] == 0:
                visit[nx][ny][z] = visit[x][y][z] + 1
                q.append((nx, ny, z))

            elif z == 0 and data[nx][ny] == 1 and visit[nx][ny][z+1] == 0:
                visit[nx][ny][z+1] = visit[x][y][z] + 1
                q.append((nx, ny, z+1))

    return visit

result = bfs(0, 0, 0)
a, b = result[n-1][m-1][0], result[n-1][m-1][1]
if a == 0 and b == 0:
    print(-1)
elif a == 0 and b != 0:
    print(b)
elif a != 0 and b == 0:
    print(a)
else:
    print(min(a, b))
