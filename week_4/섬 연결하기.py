'''
* 문제 유형 : 크루스칼 알고리즘(Union-Find 사용)

* 체감 난이도 : ***

* 아이디어 1
  - 크루스칼 알고리즘을 사용하기 위해 cost가 작은 순서대로 정렬한다.
  - union-find 알고리즘을 사용하여 사이클이 생기지 않는 간선들을 선택해 나간다.
'''

def solution(n, costs):
    answer = 0
    
    def find_parent(x, parent):
        if parent[x] != x:
            parent[x] = find_parent(parent[x], parent)
        return parent[x]
    
    def union_parent(a, b, parent):
        a = find_parent(a, parent)
        b = find_parent(b, parent)
        
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    costs = sorted(costs, key=lambda x : x[2])
    
    parent = [i for i in range(n)]
    
    for x, y, cost in costs:
        if find_parent(x, parent) != find_parent(y, parent): # 사이클 발생유무 체크
            union_parent(x, y, parent)
            answer += cost

    return answer
