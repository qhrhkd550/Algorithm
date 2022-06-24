'''
  * 아이디어 1
    - 욱제가 갈 수 있는 좌표를 구하기 위해 bfs를 사용한다.
    - 이때 벽을 피하기 위해 이미 방문했던 자리를 다시 갈 수 있으므로 visit는 없어도 된다.
    - 큐에 들어있는 개수만큼 bfs를 수행하고, 벽을 움직인다.
    - 벽을 움직일 때는 왼쪽위에서부터 탐색했으므로 순서를 뒤집어서 벽을 내린다. 그렇지 않으면 벽이 사라질 수 있다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

data = [list(map(str, input())) for _ in range(8)]

dx = [0, 1, 0, -1, -1, 1, 1, -1, 0]
dy = [1, 0, -1, 0, 1, 1, -1, -1, 0]

def move_wall():
    wall = []
    for i in range(8):
        for j in range(8):
            if data[i][j] == "#":
                wall.append((i, j))
    for i, j in wall[::-1]:
        if i+1 < 8:
            data[i+1][j] = "#"
        data[i][j] = "."

def bfs():
    q = deque()
    q.append((7, 0))

    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            if x == 0 and y == 7:
                return True

            if data[x][y] != "#":
                for i in range(9):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                        continue

                    if data[nx][ny] == "#":
                        continue

                    q.append((nx, ny))
            qlen -= 1

        move_wall()

    return False

if(bfs()):
    print(1)
else:
    print(0)
