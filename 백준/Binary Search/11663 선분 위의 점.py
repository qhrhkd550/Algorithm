'''
  * 아이디어 1
    - bisect모듈을 사용하여 right와 left의 차이가 개수이다.
    - 직접 구현해도 무관하다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
point = list(map(int, input().split()))
point.sort()
line = []
for _ in range(m):
    x1, x2 = map(int, input().split())
    line.append((x1, x2))


def binary_search(x1, x2):
    left, right = 0, 0
    start, end = 0, len(point) - 1
    while start <= end:
        mid = (start + end) // 2
        if point[mid] >= x1:
            end = mid - 1
        else:
            start = mid + 1
    left = start


    start, end = 0, len(point) - 1
    while start <= end:
        mid = (start + end) // 2
        if point[mid] > x2:
            end = mid - 1
        else:
            start = mid + 1
    right = end+1
    print(right - left)

for x1, x2 in line:
    # left = bisect_left(point, x1)
    # right = bisect_right(point, x2)
    # print(right - left)
    binary_search(x1, x2)