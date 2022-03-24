'''
* 문제 유형 : 이진탐색

* 체감 난이도 : *****

* 아이디어 1
  - 최소 시간을 이진탐색
  - 각 트럭별로 효율을 계산해서 가장 안좋은 효율을 가진 집합(gold or silver)을 포커싱해서 이진탐색 계산
  - 실패
 
* 아이디어 2
  - 최소 시간을 이진탐색
  - 현재 트럭으로 가질 수 있는 모든 금과 은을 계산하며 이진탐색
  - 단, end 는 모든 경우를 고려하여 (10**9) * (10**5) * 4로 설정 (4는 왕복 2, 금과 은을 따로 해야하는 경우 2를 고려)
  - gold, silver, total을 계산할 때, min 함수를 쓰게되면 시간이 2배가까이 증가! 
'''

def solution(a, b, g, s, w, t):
    answer = (10**9) * (10**5) * 4
    
    start = 0
    end = (10**9) * (10**5) * 4
    
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0
        
        for i in range(len(g)):
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]
            
            move = mid // (now_time * 2) # 왕복할 수 있는 횟수
            if mid % (now_time * 2) >= now_time: # 왕복하고 남은 시간이 한 번 편도할 수 있는 시간보다 크다면 횟수 + 1(운반하고 돌아오지 않아도 되기 때문!)
                move += 1
            
            if now_gold < move * now_weight: # 현재 운반할 수 있는 양이 보유한 골드량을 초과하면 보유한 골드량만큼만 추가
                gold += now_gold
            else:
                gold += move * now_weight
            
            if now_silver < move * now_weight: # 현재 운반할 수 있는 양이 보유한 실버량을 초과하면 보유한 실버량만큼만 추가
                silver += now_silver
            else:
                silver += move * now_weight
            
            if now_gold + now_silver < move * now_weight: # 현재 운반할 수 있는 양이 보유한 골드 + 보유한 실버량을 초과한다면 보유한 양만큼만 total에 추가
                total += now_gold + now_silver
            else:
                total += move * now_weight
            
        if gold >= a and silver >= b and total >= a+b: # 골드, 실버, total이 모두 만족한다면 answer 업데이트
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
