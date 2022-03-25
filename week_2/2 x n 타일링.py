'''
* 문제 유형 : DP

* 체감 난이도 : *****

* 아이디어 1
  - 규칙을 찾고 싶었지만 못찾음
  - 풀이를 참고해서 피보나치 수열과 동일하다는 점을 
'''

def solution(n):
    answer = 0
    memo = [1] * (n+1)
    
    for i in range(2, n+1):
        memo[i] = (memo[i-1] + memo[i-2]) % 1000000007
    answer = memo[n] % 1000000007
    return answer
