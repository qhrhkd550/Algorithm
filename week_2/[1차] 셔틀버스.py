'''
* 문제 유형 : 구현

* 체감 난이도 : ****

* 아이디어 1
  - 최대한 늦게 버스를 타야하므로 timetable을 정렬하고 마지막 버스 전까지 탈 수 있는 사람들은 timetable에서 모두 지우고 시작
  - 남은 사람이 한 번에 탈 수 있는 인원(m)보다 작다면 정답은 최대한 늦은 시간인 버스 출발시간이 된다.
  - 또한, 기다리고 있는 첫번째 사람이 버스 출발시간 보다 크다면 버스를 타야하므로 정답은 버스 출발시간이 된다.
  - 이러한 경우가 아닐 때, 한 번에 탈수 있는 인원 - 1 (m-1)번째 사람의 시간을 버스를 콘이 기다리는 시간으로 하고,
  - 콘이 들어갔을 경우, 콘의 위치가 m보다 크다면 1분씩 줄여나간다.
'''

from bisect import bisect_right

def solution(n, t, m, timetable):
    answer = ''
    
    # 시간 계산을 위한 함수. option은 + 또는 - 이다. +일경우 t만큼 더하고, -일경우 1분씩 뺀다.
    def time_cal(start, option):
        h, m = map(int, start.split(":"))
        if option == '+':
            if m + t >= 60:
                h += 1
                m = 0
            else:
                m += t
        else:
            if m >= 1:
                m -= 1
            else:
                h -= 1
                m = m + 60 - 1
                
        return str(h).zfill(2) + ":" + str(m).zfill(2)

    timetable.sort()
    
    start = "09:00"
    
    # 마지막 버스 전까지 탈 수 있는사람을 모두 제거
    for i in range(n-1):
        m_ = m
        while m_ > 0:
            if timetable[0] <= start:
                timetable.pop(0)
                m_ -= 1
            else:
                break
        start = time_cal(start, '+')
    
    # 남은 인원이 m보다 작거나, 첫번째로 기다리는 사람이 버스 시간보다 크다면 버스 시간이 answer
    if len(timetable) < m or timetable[0] > start:
        answer = start
    else:
        # m-1번째 시간보다 m번째 시간이 큰 경우, 콘은 m번째에 타면 되므로 m-1번째 시간 즉, timetable[m-2]번째 시간이 정답
        if timetable[m-2] < timetable[m-1]:
            answer = timetable[m-2]
        # 콘이 타는 시간을 m-1번째 사람과 같다고 가정
        else:
            answer = timetable[m-2]
            # 콘이 포함될 경우, m을 초과하는지 비교하여 만약 초과한다면 1분씩 빼면서 확인
            while True:
                index = bisect_right(timetable, answer)
                if index+1 > m:
                    answer = time_cal(answer, '-')
                else:
                    break
                
    return answer
