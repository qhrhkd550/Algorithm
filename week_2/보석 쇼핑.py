'''
* 문제 유형 : 투포인터

* 체감 난이도 : *****

* 아이디어 1
  - 현재 범위에 있는 보석들을 슬라이싱하여 보석을 전부 가져왔는지 판단
  - 시간초과
  
* 아이디어 2
  - 현재 범위의 보석을 딕셔너리로 관리
  - 모든 보석에 대해 0으로 초기화 시키고 시작
  - 모든 보석을 찾았는지 판단하기 위해 if 0 in data.values() 사용
  - 시간초과
  
* 아이디어 3
  - 투 포인터로 범위를 관리
  - 보석을 전부 찾았다면 start는 다음으로 증가
  - 현재 범위의 보석을 딕셔너리로 관리
  - 현재 가진 보석만 딕셔너리에 추가
  - start를 증가할때 이전 start가 가리키는 보석이 0개가 되어버리면 del data[gems[start]]로 딕셔너리에서 제거


'''

def solution(gems):
    answer = [-int(1e9), int(1e9)]
    s = -int(1e9)
    e = int(1e9)
    
    if len(gems) == 1:
        return [1, 1]
    
    data = {}
    jewel = len(set(gems))
    end = 0
    data[gems[0]] = 1
    
    for start in range(len(gems)):
        while len(data) < jewel and end < len(gems)-1: # 보석을 다 못찾았고, end가 더 진행할 수 있을 경우
            end += 1
            if gems[end] in data: # end가 가리키는 보석이 이미 찾은 보석이라면 +1
                data[gems[end]] += 1
            else: # end가 가리키는 보석이 처음 찾은거라면 1
                data[gems[end]] = 1
            if end == len(gems) - 1: # end가 마지막 보석이였다면, while문 종료
                break
        
        if len(data) == jewel: # 보석을 모두 찾은 경우 answer 업데이트
            if e - s > end - start:
                s, e = start, end
                
        if end == len(gems) - 1: # end가 더 이상 진행할 수 없을 경우
            if data[gems[start]] > 1: # start가 가리키는 보석이 1개 이상일 경우 -1
                data[gems[start]] -= 1
            else: # start가 가리키는 보석이 1개일 경우, 더 이상 이 보석을 제거하면 모든 보석을 못찾게되므로 그대로 종료
                break
        else: # end가 더 진행할 수 있을 경우는 start가 가리키는 보석 개수가 상관이 없다. 왜? end에서 찾을 수도 있으니까!
            if gems[start] in data: 
                if data[gems[start]] == 1: # start가 가리키는 보석이 1개라면 딕셔너리에서 해당 보석 제거
                    del data[gems[start]]
                else: # start가 가리키는 보석이 1개 이상일 경우, -1
                    data[gems[start]] -= 1
                
    return [s+1, e+1]
