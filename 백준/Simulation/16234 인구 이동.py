'''
* 아이디어 1
  - bfs를 통해 방문안한 지점에서 갈 수 있는 점들을 조사한다. 갈수있는점은 두 지점의 차이가 L과 R사이인 곳이다.
  - bfs에서 갈 수 있는 지점들을 union에 담아서 return한다.
  - 만약 bfs의 리턴이 없다면, 즉 갈 수 있는 곳이 없다면 logs에 추가하지 않는다.
  - 만약 bfs의 리턴이 존재한다면, 출발점을 추가하여 logs에 추가한다.
  - logs는 하루동안 인구이동이 일어나야하는 연합들을 관리하는 배열이다.

'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    union = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny] or abs(data[x][y] - data[nx][ny]) < l or abs(data[x][y] - data[nx][ny]) > r:
                continue

            visit[nx][ny] = True
            q.append((nx, ny))
            union.append((nx, ny))

    return union

count = 0
while True:
    visit = [[False] * n for _ in range(n)]
    logs = []
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                union = bfs(i, j)
                if union:
                    union.append((i, j))
                    logs.append(union)

    if len(logs) == 0:
        break

    for log in logs:
        tmp_sum = 0
        for x, y in log:
            tmp_sum += data[x][y]

        for x, y in log:
            data[x][y] = tmp_sum // len(log)

    count += 1

print(count)


