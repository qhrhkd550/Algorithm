'''
* 문제 유형 : 구현

* 체감 난이도 : ****

* 아이디어 1
  - 00:00:00.001 ~ 23:59:59.999를 저장할 수 있는 0.001 단위의 배열 생성
  - 모든 line에서 시간시간 ~ 끝나는시간을 index로 배열[index] += 1
  - index 0에서부터 999칸(1초)씩 sum의 max 값을 answer로 저장
  - 시간초과
 
* 아이디어 2
  - 끝나는 시간 순으로 정렬되어 있음
  - 따라서 현재 바라보는 line의 끝나는 시간 + 1초보다 나머지 line의 시작시간이 작거나 같다면 겹친다고 판단
  - 정답

'''

def solution(lines):
    answer = 0
    
    # 시작 시간을 초단위로 변환하기 위한 함수
    def start_time_cal(hh, mm, ss, interval):
        interval = interval[:-1]
        start = float(hh)*3600 + float(mm)*60 + float(ss)
        start = start - float(interval) + 0.001
        
        return start
    
    for i in range(len(lines)):
        day, time, interval = lines[i].split(" ")
        hh, mm, ss = time.split(":")
        end_second = round(float(hh)*3600 + float(mm)*60 + float(ss) + 0.999, 3)
        count = 1
        for j in range(i+1, len(lines)):
            day, time, interval = lines[j].split(" ")
            hh, mm, ss = time.split(":")
            start_second = start_time_cal(hh, mm, ss, interval)
            if start_second <= end_second:
                count += 1
                
        answer = max(answer, count)
    return answer
