'''
  * 아이디어 1
    - 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다. -> 처음 data를 입력받는 것과 같다.
    - 다음 1초 동안 봄버맨은 아무것도 하지 않는다. -> 아무것도 하지 않기 때문에, n -= 1을 수행한다.
    - 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
        -> 다음 차례에 폭탄을 터뜨려야하기 때문에 현재 폭탄의 위치를 찾고(findBoom), 빈칸에 전부 폭탄을 설치한다(setBoom). 
    - 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다. -> findBoom으로 찾은 폭탄을 터뜨린다(Boom).
    - 3과 4를 반복한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

r, c, n = map(int, input().split())
data = [list(map(str, input())) for _ in range(r)]
n -= 1

def findBoom():
    BoomList = deque()
    for i in range(r):
        for j in range(c):
            if data[i][j] == 'O':
                BoomList.append((i, j))
    
    return BoomList

def setBoom():
    for i in range(r):
        for j in range(c):
            if data[i][j] != 'O':
                data[i][j] = 'O'

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def Boom():
    for x, y in BoomList:
        data[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                data[nx][ny] = '.'

while n:
    BoomList = findBoom()
    setBoom()
    n -= 1
    if n == 0:
        break
    Boom()
    n -= 1

for i in range(r):
    for j in range(c):
        print(data[i][j], end='')
    print()