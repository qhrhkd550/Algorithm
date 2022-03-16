'''
* 문제 유형 : 그래프

* 체감 난이도 : **

* 아이디어 1
  - 주어진 2차원 배열을 연결 리스트(grpah)로 변환하여 bfs 수행

* 아이디어 2
  - 주어진 2차원 배열을 그대로 bfs 수행
  
* 다른 풀이
  - union-find 알고리즘을 수행해도 가능
  - 단, 1-2-3-4-5 처럼 연결 된 그래프는 parent 배열의 모든 원소 값이 1이 아니라 1, 1, 2, 3, 4이기 때문에 각 노드별로 find 함수를 호출하면 정답
'''

from collections import deque

def solution(n, computers):
    answer = 0
    
    def bfs(x):
        q = deque()
        q.append(x)
        visit[x] = True
        
        while q:
            x = q.popleft()
            for i in graph[x]:
                if not visit[i]:
                    visit[i] = True
                    q.append(i)

#         2차원 배열을 그대로 사용할 경우
#         while q:
#             x = q.popleft()
#             for i in range(n):
#                 if computers[x][i] == 1 and not visit[i]:
#                     visit[i] = True
#                     q.append(i)

    # 2차원 배열을 그대로 사용할 경우 43~48번 line은 주석 가능
    graph = [set() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].add(j)
                graph[j].add(i)

    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            bfs(i)
            answer += 1
        
    return answer
