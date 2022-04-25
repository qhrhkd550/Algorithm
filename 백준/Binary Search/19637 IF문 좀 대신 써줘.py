'''
  * 아이디어 1
    - 전형적인 이진 탐색 문제이다.
    - 해당 값이 어디 들어갈 수 있는지 확인하면 되기 때문에
    - bisect_left 를 사용해도 되고, 직접 작성해도 무방하다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from bisect import bisect_left

n, m = map(int, input().split())
rank = []
condition = []
for _ in range(n):
    r, c = input().split(' ')
    c = int(c)
    rank.append(r)
    condition.append(c)

power = []
for _ in range(m):
    power.append(int(input()))


def binary_search(p):
    start, end = 0, len(condition)-1
    while start <= end:
        mid = (start + end) // 2
        if condition[mid] >= p:
            end = mid - 1
        else:
            start = mid + 1
    print(rank[start])

for p in power:
    # left = bisect_left(condition, p)
    # print(rank[left])
    binary_search(p)

