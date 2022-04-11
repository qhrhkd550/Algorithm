'''
* 문제 유형 : 그리디

* 체감 난이도 : ***

* 아이디어 1
  - 고속도로에 먼저 들어오고, 먼저 나가는 순서대로 정렬한다.
  - 처음 고속도로에 진입하는 차라면 단속 카메라를 첫 차가 나가는 지점으로 설정한다.
  - 나머지 차들의 경우 현재 존재하는 모든 단속 카메라와 비교한다.
  - 만약, 단속카메라가 현재 차의 범위내에 있다면 추가 설치가 필요없다.
  - 만약, 단속카메라가 현재 차가 고속도로를 빠져나간 후에 있다면 해당 카메라를 현재 차의 end시점으로 바꾸고 추가 설치가 필요없다.
  
* 아이디어 2
  - 고속도로에서 나가는 시간을 기준으로 정렬한다.
  - 처음 고속도로에 진입하는 차라면 단속카메라를 첫차가 나가는 지점으로 설정한다.
  - 나머지 차들의 경우, 진입시간이 마지막 카메라 위치보다 작으면 설치가 필요없고, 크다면 해당 차가 나가는 지점에 카메라를 설치한다.
    def solution(routes):
      routes = sorted(routes, key=lambda x: x[1])
      last_camera = -30000

      answer = 0

      for route in routes:
          if last_camera < route[0]:
              answer += 1
              last_camera = route[1]

      return answer
'''

def solution(routes):
    answer = []
    routes = sorted(routes, key=lambda x : (x[0], x[1]))
    
    for start, end in routes:
        if not answer: # 첫 차라면 카메라를 나가는 지점에 설치
            answer.append(end)
        else:
            flag = False
            for i in range(len(answer)): # 현재 설치된 모든 카메라 중
                if start <= answer[i] <= end: # 카메라가 경로상에 있다면 추가 설치 필요없다
                    flag = True
                    break
                elif end < answer[i]: # 카메라가 해당차량의 나가는 지점보다 뒤에 있다면 해당 차량이 나가는 시간으로 카메라 위치를 바꾸면 추가 설치 필요없다.
                    answer[i] = end
                    flag = True
                    break
            
            if not flag:
                answer.append(end)
    
    return len(answer)
