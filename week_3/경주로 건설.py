'''
* 문제 유형 : BFS

* 체감 난이도 : ****

* 아이디어 1
  - 최소값을 구하는 문제이기 때문에 BFS 알고리즘을 선택
  - 단, 상하좌우로 움직일 수 있기 때문에 visit 배열은 각 방향에서 오는 값을 모두 저장할 수 있도록 4개의 값을 가진다. (3차원)
  - bfs 첫 큐에 시작점 (0,0)에서 갈 수 있는 오른쪽, 아래쪽을 넣어주고, visit[0][0][1], visit[0][0][2]를 0으로 초기화한다.
  - 다음 갈 수 있는 좌표에서 방향을 따져 직선이라면 visit[nx][ny][갈 방향] > visit[nx][ny][이전 방향] + 100 이라면 visit[nx][ny][갈 방향] 을 업데이트.
  - 다음 갈 수 있는 좌표에서 방향을 따져 곡선이라면 visit[nx][ny][갈 방향] > visit[nx][ny][이전 방향] + 600 이라면 visit[nx][ny][갈 방향] 을 업데이트.
  - 마지막 결과값은 visit[n-1][n-1] 의 최소값이 된다.
'''

from collections import deque

def solution(board):
    answer = 0
    
    n = len(board)
    
    # 상 우 하 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    def bfs():
        q = deque()
        q.append((0, 0, 1))
        q.append((0, 0, 2))
        visit[0][0][1] = 0
        visit[0][0][2] = 0
        
        while q:
            x, y, d = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == 1:
                    continue
                
                if ((d == 0 or d == 2) and (i == 1 or i == 3)) or ((d == 1 or d == 3) and (i == 0 or i == 2)):
                    if visit[nx][ny][i] > visit[x][y][d] + 600:
                        visit[nx][ny][i] = visit[x][y][d] + 600
                        q.append((nx, ny, i))
                else:
                    if visit[nx][ny][i] > visit[x][y][d] + 100:
                        visit[nx][ny][i] = visit[x][y][d] + 100
                        q.append((nx, ny, i))
    
    visit = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]
    bfs()
    answer = min(visit[n-1][n-1])
    return answer
