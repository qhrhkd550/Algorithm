'''
* 문제 유형 : dfs

* 체감 난이도 : ****

* 아이디어 1
  - 시작점과 상관없이 가장 깊이 있는 노드들부터 처리하면 된다.
  - visit[시작점]을 True로 바꾸지 않고 통과되는 이유는, now와 next 노드의 값을 계산할때, next 노드의 값을 0 으로 만들기 떄문에
  - 다시 방문했을때 결과에 영향을 미치지 않는다.

'''

import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict

def solution(a, edges):
    answer = 0
    
    graph = [[] for _ in range(len(a))]
    data = defaultdict(int)
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    def dfs(now):
        nonlocal answer
        
        for next in graph[now]:
            if not visit[next]:
                visit[next] = True
                if dfs(next):
                    a[now] += a[next]
                    answer += abs(a[next])
                    a[next] = 0
                    
                visit[next] = False
        
        return True

    visit = [False] * len(a)
    start = 0
    dfs(start)
    if a[start] != 0: # 시작점 값이 0이 아니라면 모두 0으로 만들 수 없는 경우이다.
        answer = -1
        
    return answer
