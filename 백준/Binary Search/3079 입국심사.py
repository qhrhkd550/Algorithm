'''
  * 아이디어 1
    - 입국 심사에 걸리는 총 시간을 이분탐색한다.
    - 최소시간은 1, 최대시간은 가장 긴 시간을 소요하는 심사관이 모든 사람을 처리하는 시간이다.
    - 해당 시간에 각 심사관이 맡을 수 있는 사람의 수를 count한다.
    - count가 m보다 크거나 같다면 시간을 줄여도 된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
T = [int(input()) for _ in range(n)]

start, end = 1, max(T)*m
answer = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for t in T:
        count += mid // t

    if count >= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)
