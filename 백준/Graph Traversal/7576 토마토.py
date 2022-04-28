'''
  * 아이디어 1
    - 모든 토마토는 동시에 주변에 영향을 미치기 때문에, 현재 큐의 길이만큼 주변 토마토를 익히는 작업을 수행하고 날짜를(count) 추가한다.
    
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(q):
    count = -1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if data[nx][ny] == -1 or data[nx][ny] == 1:
                    continue
                
                data[nx][ny] = 1
                q.append((nx, ny))
            qlen -= 1
        
        count += 1
    
    return count

def check():
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                return False
    return True


tomato = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            tomato.append((i, j))

answer = bfs(tomato)
if check():
    print(answer)
else:
    print(-1)