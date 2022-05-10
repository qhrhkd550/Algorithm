'''
  * 아이디어 1
    - 0 ~ 100000 까지의 방문 배열을 생성 후, bfs를 통해 탐색한다.
    - 단, x*2의 우선순위를 높이기 위해 x*2를 먼저 탐색하도록 한다.
    - x * 2의 경우 0, x + 1, x - 1의 경우는 visit[x] + 1 을 추가한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, k = map(int, input().split())
def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = 0

    while q:
        x = q.popleft()
        if x == k:
            return visit[x]

        for i in [x*2, x-1, x+1]:
            if 0 <= i < 100001 and visit[i] == -1:
                if i == x * 2:
                    visit[i] = visit[x]
                else:
                    visit[i] = visit[x] + 1
                q.append(i)


visit = [-1] * 100001
answer = bfs(n)
print(answer)