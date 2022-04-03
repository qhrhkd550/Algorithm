'''
* 체감 난이도 : **

* 아이디어 1
  - 최단거리가 k 인 지점들을 출력해야 하므로,
  - k번만큼만 bfs를 수행한다.

* 주의
  - if len(answer) == 0: 을 하게되면 런타임 에러가 발생한다...
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visit = [False] * (n+1)
def bfs(start, k):
    q = deque()
    q.append(start)
    visit[start] = True

    while q:
        q_len = len(q) # 현재 큐 길이만큼만 새로운 노드를 탐색하기 위해서 큐의 길이를 측정

        while q_len:
            x = q.popleft()
            for next_ in graph[x]:
                if not visit[next_]:
                    visit[next_] = True
                    q.append(next_)
            q_len -= 1

        k -= 1 # 한 번 수행할 때마다 길이 - 1
        if k == 0: # k == 0 일때 큐에 있는 노드들이 최단거리 k로 갈 수 있는 노드들이다.
            return q

answer = bfs(x, k)
if not answer:
    print(-1)
else:
    answer = sorted(answer)
    for a in answer:
        print(a)