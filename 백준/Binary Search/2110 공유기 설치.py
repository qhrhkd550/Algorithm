'''
  * 아이디어 1
    - 인접한 거리를 최대화 해야하기 때문에 이 거리를 이분탐색 한다.
    - 주어진 데이터를 정렬하면 즉, 집을 오름차순 정렬하면 거리의 최소값은 1, 최대값은 마지막집과 첫번째집의 차이값이다.
    - 항상 첫번째 집에는 공유기를 설치하면되므로, 현재 공유기가 설치된 지점을 의미하는 value = x[0], 공유기 설치 개수인 count = 1로 설정한다.
    - 두번째집부터 만약 현재 공유기위치에서 mid(거리)를 더한지점이 두번째집보다 작다면, 설치하면되니까 value를 업데이트하고 count + 1한다.
    - count가 c보다 작다면 거리를 줄여야 하고, c보다 크거나 같다면 늘려야한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

# 1 2 4 8 9
start, end = 1, x[-1] - x[0]
while start <= end:
    mid = (start + end) // 2
    value = x[0]
    count = 1
    for i in range(1, n):
        if x[i] >= value + mid:
            value = x[i]
            count += 1

    if count < c:
        end = mid - 1
    elif count >= c:
        start = mid + 1

print(end)