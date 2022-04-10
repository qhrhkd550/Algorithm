'''
* 체감 난이도 : **

* 아이디어 1
  - 이진탐색 구현 -> 전형적인 이진탐색

* 아이디어 2
  - bisect 모듈사용 -> right - 1 == left면 값을 찾았다는 뜻.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from bisect import bisect_left, bisect_right

n = int(input())
card = list(map(int, input().split()))
m = int(input())
check_card = list(map(int, input().split()))

card.sort()

def binary_search(num):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if card[mid] > num:
            end = mid - 1
        elif card[mid] == num:
            print(1, end= ' ')
            return
        else:
            start = mid + 1
    print(0, end=' ')
    return

# 방법 1 - 이진탐색 구현
for check in check_card:
    binary_search(check)

# 방법 2 - bisect 모듈 사용
# for check in check_card:
#     left = bisect_left(card, check)
#     right = bisect_right(card, check)
#     if right - 1 == left:
#         print(1, end = ' ')
#     else:
#         print(0, end = ' ')
