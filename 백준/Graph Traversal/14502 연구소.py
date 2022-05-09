'''
  * 아이디어 1
    - 전체 플로우는 아래와 같다.
      1. 초기 바이러스의 위치를 찾는다. (앞으로 복사해서 사용할 예정)
      2. 벽을 3개 세운다.
      3. 바이러스를 퍼뜨린다.
      4. 안전구역 개수를 찾는다.

    - 조합으로 이차원의 모든 좌표를 고려하며 dfs를 통해 벽 3개의 위치를 선정한다.
    - 바이러스를 퍼뜨리기 위해 bfs를 사용한다.

  * 주의할점
    - 맵을 복사해서 써야하므로 copy를 해야하는데 .copy()는 얕으복사가 되므로 사용해선 안된다.
    - copy.deepcopy(data)를 사용해야한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

virus_list = deque()
def find_virus():
    for i in range(n):
        for j in range(m):
            if data[i][j] == 2:
                virus_list.append((i, j))

    return virus_list

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

import copy
def spread_virus():
    tmp_data = copy.deepcopy(data)
    tmp_virus_list = copy.deepcopy(virus_list)

    while tmp_virus_list:
        x, y = tmp_virus_list.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_data[nx][ny] != 0:
                continue

            tmp_data[nx][ny] = 2
            tmp_virus_list.append((nx, ny))

    find = 0
    for i in range(n):
        for j in range(m):
            if tmp_data[i][j] == 0:
                find += 1
    return find

answer = 0

def dfs(start, count):
    global answer
    if count == 3:
        answer = max(answer, spread_virus())

        return


    for i in range(start, n*m):
        x = int(i / m)
        y = int(i % m)
        if data[x][y] == 0:
            data[x][y] = 1
            dfs(i + 1, count + 1)
            data[x][y] = 0

find_virus() # 초기 바이러스 위치
dfs(0, 0)
print(answer)
