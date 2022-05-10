'''
  * 아이디어 1
    - Simulation의 인구이동 문제와 동일하기 때문에 설명 생략
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, L, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, visit):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    total = data[x][y]
    path = [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visit[nx][ny]:
                continue

            if L > abs(data[x][y] - data[nx][ny]) or abs(data[x][y] - data[nx][ny]) > R:
                continue

            visit[nx][ny] = True
            q.append((nx, ny))
            total += data[nx][ny]
            path.append((nx, ny))

    if len(path) > 1:
        for x, y in path:
            data[x][y] = total // len(path)
        return True

    return False

def run():
    answer = 0
    flag = False
    while True:
        visit = [[False] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if not visit[i][j]:
                    if bfs(i, j, visit):
                        flag = True

        answer += 1

        if not flag:
            break
        else:
            flag = False

    return answer



answer = run()
print(answer-1)



