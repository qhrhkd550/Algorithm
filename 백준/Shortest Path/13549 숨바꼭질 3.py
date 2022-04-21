'''
* 아이디어 1
  - 최소값을 찾는 문제이므로 BFS를 이용한다.
  - 단, x*2의 경우 가중치가 0 이고, x+1, x-1의 경우 가중치가 1이기때문에
  - x*2 연산부터 우선적으로 처리하도록 한다.
  - 이렇게 하지 않으면 메모리초과가 발생한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, k = map(int, input().split())
visit = [-1] * 100001

def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = 0

    while q:
        x = q.popleft()
        if x == k:
            print(visit[x])
            return

        for nx in (x*2, x-1, x+1):
            if nx < 0 or nx >= 100001:
                continue

            if visit[nx] != -1:
                continue

            if nx == x*2:
                visit[nx] = visit[x]
            else:
                visit[nx] = visit[x] + 1
            q.append(nx)

bfs(n)