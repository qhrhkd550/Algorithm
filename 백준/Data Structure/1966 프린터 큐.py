'''
* 아이디어 1
  - 큐에서 작업을 뺄때마다 m도 1씩빼면된다.
  - m이 다시 큐의 마지막으로 가야할때는 n-1이 아니라, 현재 큐의 길이-1 이 되어야한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    count = 0
    while True:
        now = queue.pop(0) # 현재 볼 작업
        m -= 1 
        if queue and max(queue) > now: # 우선선위가 높은 작업이 남아있다면
            queue.append(now) # 큐의 마지막에 다시 삽입
            if m == -1: # 현재작업이 m이 가리키는 작업이라면 큐의 마지막 인덱스로 수정
                m = len(queue) - 1

        else: # 우선순위가 높은게 없다면
            count += 1 # 출력횟수 증가
            if m == -1: # 현재 작업이 출력되었다면
                print(count) # 출력횟수 출력하고 종료
                break