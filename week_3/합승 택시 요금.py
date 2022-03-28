'''
* 문제 유형 : 최단 거리 알고리즘(다익스트라, 플로이드와샬 등)

* 체감 난이도 : ****

* 아이디어 1
  - ex) s = 1, a = 4, b = 5 라고 할 때, 3까지 합승 후, 각 a, b까지 가는 경우는
  - s->3까지의 최단 거리 + 3->a까지 최단거리 + 3->b 까지 최단거리를 의미한다.
  - 즉, 주어진 맵으로 플로이드 와샬 알고리즘을 통해 각 점에서부터의 최단거리를 구한다.
'''

def solution(n, s, a, b, fares):
    answer = int(1e9)
    
    data = [[int(1e9)] * n for _ in range(n)]
    for x, y, cost in fares:
        data[x-1][y-1] = cost
        data[y-1][x-1] = cost
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    data[i][j] = min(data[i][j], data[i][k] + data[k][j])
       
    # 합승할 수 있는 노드
    for i in range(n):
        together = 0 if s-1 == i else data[s-1][i] # 출발지와 경유지가 같다면 0
        go_a = 0 if i == a-1 else data[i][a-1] # a와 경유지가 같다면 0
        go_b = 0 if i == b-1 else data[i][b-1] # b와 경유지가 같다면 0
        answer = min(answer, together + go_a + go_b)
        
    return answer
