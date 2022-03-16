'''
* 문제 유형 : 이진탐색

* 체감 난이도 : ****

* 아이디어 1
  - ex) 주어진 예시에서 최대 시간인 10 * 6 을 end로 이진탐색을 수행
  - 7과 10으로 가능한 수를 만들기 위해 각 n // 2명씩 할당 -> [7, 10, 14, 20, 21, 28] 배열 생성
  - mid 보다 작거나 같은 배열의 원소 개수를 mid와 비교하여 end, start값 조정
  - 배열을 만드는 경우 시간초과
 
* 아이디어 2
  - 아이디어 1과 이진탐색은 동일
  - mid // 7 + mid // 10 = 심사 가능한 사람의 수(possible)
  - possible과 mid를 비교하여 이진탐색 수행
  
'''

def solution(n, times):
    answer = int(1e9)
    start, end = 0, max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        possible = 0
        for t in times:
            possible += mid // t
        
        if possible >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
