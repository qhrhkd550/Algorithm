'''
* 문제 유형 : 탐색

* 체감 난이도 : ****

* 아이디어 1
  - ICN에서 시작해 계속 다음 도시로 갈 수 있다면, 경로를 가리키는 tmp에 추가
  - 만약 더 이상 진행할 수 없다면, tmp에서 제거 후, answer에 추가
  - 위 과정을 수행하면 answer는 방문의 역순이 저장
  - 즉, 더 이상 갈 수 없는 지점을 탐색하여 방문 순서의 역순을 찾는 문제!
'''

from collections import defaultdict

def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
            
    for key in graph.keys():
        graph[key].sort()
    
    tmp = ["ICN"]
    while tmp:
        now = tmp[-1]
        if now not in graph or not graph[now]:
            answer.append(tmp.pop(-1))
        else:
            tmp.append(graph[now].pop(0))
            
    return answer[::-1]
