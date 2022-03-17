'''
* 문제 유형 : 구현

* 체감 난이도 : ***

* 아이디어 1
  - SJF 스케쥴링 알고리즘을 사용
  - 현재 작업이 종료되는 시간(end_time)까지 들어온 작업들을 heapq에 삽입(작업 소요시간을 기준)
'''

import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)
    jobs = sorted(jobs, key=lambda x:(x[0], x[1]))
    
    def SJF():
        nonlocal answer
        nonlocal end_time
    
        q = []
        arrive, request = jobs.pop(0)
        heapq.heappush(q, (request, arrive)) # 작업요청시간을 기준으로 heapq에 삽입해야하므로, (request, arrive) 삽입

        while q:
            request, arrive = heapq.heappop(q) # 현재 작업하는 job
            
            if arrive > end_time: # 현재 job의 도착시간이 이전 작업이 끝난시간보다 뒤라면 (arrive - end_time) 추가
                end_time = end_time + request + (arrive - end_time)
            else:
                end_time = end_time + request
                
            while jobs:
                if jobs[0][0] <= end_time: # 다음 job의 도착 시간이 현재 job이 끝나는 시간보다 전이라면 heapq에 삽입
                    next_arrive, next_request = jobs.pop(0)
                    heapq.heappush(q, (next_request, next_arrive))
                else:
                    break
            answer += end_time - arrive
    
    
    end_time = 0
    while jobs: # 현재 job과 다음 job사이에 공백이 있을 수 있기 때문에, jobs가 남아있다면 SJF 함수 호출
        SJF()
    
    return answer // length
