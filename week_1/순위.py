'''
* 문제 유형 : 그래프

* 체감 난이도 : ****

* 아이디어 1
  - A->B : A가 B를 이김
  - 1 -> 2, 2 -> 5 일 경우, 1->5 가 성립
  - 따라서 플로이드 와샬 알고리즘 사용
'''

def solution(n, results):
    answer = 0
    
    graph = [[0] * n for _ in range(n)]
    for r1, r2 in results:
        graph[r1-1][r2-1] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and graph[i][j] == 0:
                    if graph[i][k] == 1 and graph[k][j] == 1: # 1 이면 이기는 것을 의미
                        graph[i][j] = 1
                    
    for win, lose in zip(graph, zip(*graph)):
        if sum(win) + sum(lose) == n-1:
            answer += 1
        
    return answer
