'''
* 문제 유형 : 해시, 구현

* 체감 난이도 : **

* 아이디어 1
  - 추천자는 한명이기 때문에 각 enroll별로 추천자가 누구인지 dict로 관리 (data)
  - 각 enroll별로 총 수입 관리 (enroll_income)
  - 현재 수입에 대해 추천자가 '-' 가 아닐 때까지 10%씩 위로 줌
  - 단, 시간초과 문제를 해결하기 위해 원단위가 아닌 금액 즉, remain = 0일때 종료
'''

from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    
    data = defaultdict(str)
    enroll_income = defaultdict(int)
    for e, r in zip(enroll, referral):
        data[e] = r
    
    
    for s, a in zip(seller, amount):
        income = a * 100
        now = s
        while True:
            remain = int(income * 0.1)
            enroll_income[now] += income - remain
            income = remain
            now = data[now]
            
            if now == '-' or remain == 0:
                break
    
    for e in enroll:
        answer.append(enroll_income[e])
                
    return  answer
