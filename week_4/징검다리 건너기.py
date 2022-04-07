'''
* 문제 유형 : 이분 탐색

* 체감 난이도 : ****

* 아이디어 1
  - 이분 탐색의 대상을 건널 수 있는 사람의 수(mid)로 설정
  - stone이 mid보다 작은 경우가 연다라 k번나오면 mid명 만큼 못건넌다는 뜻이므로 end를 줄인다.
  - 반대로 연다라 k번 나오지 않는다면 start를 늘린다.

* 주의사항
  - stone과 mid를 비교하여 k번 나오는지 탐색하는 과정을 함수로 만들게 되면 7번, 12번 테스트케이스가 시간초과가 발생한다..
'''

def solution(stones, k):
    answer = 0
    
    start, end = 0, max(len(stones), max(stones))

    while start <= end:
        mid = (start + end) // 2
    
        count = 0
        flag = True
        for i in range(len(stones)):
            if stones[i] <= mid:
                count += 1
                if count == k:
                    flag = False
                    break
            else:
                count = 0
        
        if not flag:
            end = mid - 1
        else:
            start = mid + 1
                    
    return start
