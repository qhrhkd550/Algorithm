'''
* 문제 유형 : DP

* 체감 난이도 : ***

* 아이디어 1
  - DFS 이용
  - ex) 5를 연속으로 붙이는 경우 계산 불가능
  
* 아이디어 2
  - ex) 1 ~ 12 를 저장할 수 있는 DP 배열 생성 후, 5를 이용해 각 수를 만들 수 있는 최소 경우를 계산
  - 모든 경우를 계산할 수 없기 때문에, 점화식 불가능 판단
  
* 아이디어 3
  - ex) 1 ~ 12 를 저장할 수 있는 DP 배열 생성 후, 5를 index 번 사용해 만들 수 있는 모든 값을 저장
  - 연산자를 ['.', '-', '*', '//']로 두었을 경우, 55+5/5 와 같은 식은 만들 수 있었지만, 연산자 우선순위 부여 불가능
  
* 아이디어 4
  - ex) 1 ~ 12 를 저장할 수 있는 DP 배열 생성 후, 5를 index 번 사용해 만들 수 있는 모든 값을 저장
  - index = 3 인 경우(5를 3번 사용하는 경우), 5를 (1, 2), (2, 1)번 사용한 경우를 고려
  - DP[3] = (DP[1] 과 DP[2]를 product 하여 사칙연산 수행) + (DP[2] 과 DP[1]를 product 하여 사칙연산 수행) + (5를 3번 붙인 경우)
  - 주의! 연산자가 // 일때 0으로 나누는 경우, 예외처리
  - DP[i]번째 계산이 완료 되었을 경우, number의 존재여부 확인 후 return
  
* 개선방향
  - DP[5] 인 경우, (1, 4), (2, 3), (3, 2), (4, 1)을 전부 고려하지만, 
  - 경우의 수를 반으로 줄이기 위해 (//, -) 연산 수행 시 (A // B, B // A), (A - B, B - A) 과 같이 양방향 처리할 수 있음
  - 또한, DP[i]를 전부 계산하기 전, 연산을 한 번 수행할 때마다 number와 값 비교 가능

'''
from itertools import product

def solution(N, number):
    answer = 0
    oper = ['+', '-', '*', '//']
    memo = [set() for _ in range(9)] # 중복된 값을 처리하기 위해 set 자료구조 사용
    memo[1].add(N)
    
    if N == number:
        return 1
    
    for i in range(2, 9):
        
        memo[i].add(int(str(N) * i)) # N을 i번 붙인 경우를 추가
        
        for j in range(1, i): # i를 만들기 위한 숫자 두개 조합 (j, i-j)
            for p1, p2 in product(memo[j], memo[i-j]):
                for o in oper:
                    if o == '//':
                        if p2 != 0:
                            memo[i].add(eval(str(p1) + o + str(p2)))
                    else:
                        memo[i].add(eval(str(p1) + o + str(p2)))
                
        if number in memo[i]:
            return i
        
    return -1
