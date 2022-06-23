'''
  * 아이디어 1
    - 1인 모든 지점에서 가장자리 여부를 확인한다.
    - bfs를 통해 가장자리 여부를 확인한다.
    - 갈 수 있는 곳 중, 1이 아니고 방문하지 않은 지점만 큐에 넣는다.
    - 만약 좌표가 끝에 도달하면 가장자리로 판단한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == 0 or nx == n-1 or ny == 0 or ny == m-1:
                return True

            if data[nx][ny] != 1 and not visit[nx][ny]:
                q.append((nx, ny))

            visit[nx][ny] = True

    return False

one_hour = 0
time = 0
while True:
    remove = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                visit = [[False] * m for _ in range(n)]
                res = bfs(i, j)
                if res: # 가장자리
                    remove.append((i, j))

    if remove:
        one_hour = len(remove)
        for x, y in remove:
            data[x][y] = 0

    else:
        print(time)
        print(one_hour)
        break

    time += 1