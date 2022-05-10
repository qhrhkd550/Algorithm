'''
  * 아이디어 1
    - bfs를 통해 (1,1)에서 (n,m)까지의 최단거리를 구하면 된다.
    - 단, bfs탐색 중, 2(그람)을 만났을 경우, 찾았다는 표시(find = True)와 그람의 좌표(gram)을 저장해야한다.
    - 이유는 탐색이 끝났을 경우, 그람을 통해서 가는 경우와 그람없이 탐색하는 경우 중 최소값을 찾아야 하기 때문이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    global gram, find
    q = deque()
    q.append((x, y))
    visit[x][y] = 0

    while q:
        x, y = q.popleft()

        if data[x][y] == 2: # 만약 그람을 찾았다면, 그람의 좌표를 저장하고 찾았다는 표시를 해준다.
            gram = [x, y]
            find = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if data[nx][ny] == 1 or visit[nx][ny] != -1:
                continue

            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))



visit = [[-1] * m for _ in range(n)]
gram = [0, 0] # 그람의 좌표
find = False # 그람을 찾았는지 여부
answer = 0
bfs(0, 0)
x, y = gram[0], gram[1]
use_gram = visit[x][y] + abs(x - (n-1)) + abs(y - (m-1)) # 그람을 찾았다면, 그람의 위치와 공주 위치의 맨허튼 거리가 최단거리이다.
not_use_gram = visit[n-1][m-1]

if not_use_gram == -1: # 만약 공주를 찾지 못한 경우
    if find: # 그람을 찾았다면
        if use_gram > t: # 그람을 사용했을 때, t를 초과한 경우 Fail 출력
            print("Fail")
        else: # t를 초과하지 않은 경우, use gram 출력
            print(use_gram)
    else: # 공주도 못찾고 그람도 못찾은 경우 Fail 출력
        print("Fail")

else: # 공주를 찾은 경우,
    answer = min(use_gram, not_use_gram) # 그람을 사용한 경우와 그냥 찾은 경우의 최소값 선택
    if answer > t: # 최소값이 t 초과라면 Fail
        print("Fail")
    else:
        print(answer)