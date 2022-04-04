'''
* 문제유형 : 구현 + bfs

* 체감 난이도 : ****

* 아이디어 1
  - bfs를 통해 game_board에 있는 도형 하나를 선택한다. -> 도형의 좌표를 리턴
  - 선택한 도형에 대해서 table에 있는 도형을 매칭시켜본다.
  - table은 회전시킬 수 있으므로 4방향에 대해서 전부 매칭시켜본다.
  - 도형이 같은지 확인하는 방법은 리턴받은 두 도형의 좌표를 각 도형의 시작좌표로 뺄셈하게되면 같은 도형일 경우, 값이 같아진다.
  ex) 도형1 시작좌표 : 0, 2 도형좌표 : (0, 2), (0, 3), (1, 3), (2, 3), (2, 4) 뺄셈 결과 : (0, 0), (0, 1), (1, 1) ~~
      도형2 시작좌표 : 0, 3 도형좌표 : (0, 3), (0, 4), (1, 4), (2, 4), (2, 5) 뺄셈 결과 : (0, 0), (0, 1), (1, 1) ~~
      
'''

from collections import deque

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # 도형 하나를 추출하는 함수 (bfs)
    def check_puzzle(i, j, base, tmp, visit): # i, j 는 시작좌표, base는 board_game은 0, table은 1, tmp는 탐색해야하는 테이블, visit는 탐색해야하는 visit table 
        q = deque()
        q.append((i, j))
        visit[i][j] = True
        move = [(i, j)] # 도형이 이동한 좌표를 저장
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if visit[nx][ny] or tmp[nx][ny] != base:
                    continue
                visit[nx][ny] = True
                q.append((nx, ny))
                move.append((nx, ny))
        
        return move
        
    # table을 90도씩 회전하는 함수
    def rotation(table):
        tmp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tmp[j][n-i-1] = table[i][j]
        return tmp
    
    # table의 도형을 하나씩 탐색하여 puzzle과 매칭되는지 확인하는 함수
    def check_True(table, puzzle, pi, pj):
        visit_table = [[False] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if table[x][y] == 1 and not visit_table[x][y]:
                    tpuzzle = check_puzzle(x, y, 1, table, visit_table)
                    tmp1, tmp2 = [], [] # game_board의 puzzle과 table의 tpuzzle이 동일한 도형인지 확인하기 위한 리스트
                    # 각 도형의 시작 좌표를 뺀다.
                    for px, py in puzzle: 
                        tmp1.append((pi-px, pj-py))
                    for tx, ty in tpuzzle:
                        tmp2.append((x-tx, y-ty))
                    if tmp1 == tmp2: # 두 도형이 일치하면, table에서 해당 도형을 제거 후, return True
                        for i, j in tpuzzle:
                            table[i][j] = 0
                        return True
    
    visit = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visit[i][j]: # game_board에서 도형을 하나 선택한다.
                puzzle = check_puzzle(i, j, 0, game_board, visit) # puzzle은 도형의 좌표를 리턴받는다.
                for _ in range(4): # table을 4번 회전시키면서 매칭되는 도형이 있는지 확인
                    table = rotation(table)
                    if check_True(table, puzzle, i, j): # 회전된 table에서 도형을 하나씩 puzzle과 비교하여 매칭된다면 return True
                        answer += len(puzzle)
                        break # game_board의 해당 도형이 매칭이 됐다면, 더 이상 이 도형에 대해 탐색할 필요없으므로 break
                                 
    return answer
