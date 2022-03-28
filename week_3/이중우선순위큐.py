'''
* 문제 유형 : heapq

* 체감 난이도 : **

* 아이디어 1
  - 최대값 삭제와 최소값 삭제가 있으므로 max_q, min_q를 따로 관리
  - 단, 하나의 큐에서 값이 삭제될 때, 다른 큐에서도 같은 값을 제거

* 주의사항
  - heapq 자료구조는 최소힙을 기반으로 한다. 하지만, heapq[-1]이 최대값을 의미하는 것은 아니기 때문에,
  - answer를 구할 때, 인덱스로 접근하면 안된다.
'''

import heapq

def solution(operations):
    answer = []
    
    max_q = []
    min_q = []
    for operation in operations:
        if "I" in operation:
            num = int(operation.split(" ")[1])
            heapq.heappush(max_q, -num)
            heapq.heappush(min_q, num)
        
        elif max_q and operation == "D 1":
            max_value = -heapq.heappop(max_q)
            min_q.remove(max_value)
        
        elif min_q and operation == "D -1":
            min_value = heapq.heappop(min_q)
            max_q.remove(-min_value)
    
    if len(min_q) >= 1:
        answer = [max(min_q), min(min_q)]
    else:
        answer = [0, 0]
    return answer
