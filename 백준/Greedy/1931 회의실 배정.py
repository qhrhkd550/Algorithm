'''
  * 아이디어 1
    - 최대한 많은 회의를 진행해야하므로 회의가 빨리 끝나는 시간순으로 정렬한다.
    - 단 회의가 끝나자마자 바로 시작될 수 있으므로 비교할때는 =를 포함해야한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time = sorted(time, key=lambda x : (x[1], x[0]))

start, end = 0, 0
answer = 0
for s, e in time:
    if end <= s:
        start, end = s, e
        answer += 1

print(answer)