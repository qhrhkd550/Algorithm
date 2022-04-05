'''
* 체감 난이도 : *

* 아이디어 1
  - 1~N까지의 숫자를 담은 deque 생성 후, popleft와 append(popleft)를 반복 수행한다.
  - 단, deque가 아닌 list를 사용할 경우 시간초과 발생
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import deque

n = int(input())
card = deque()
for i in range(1, n+1):
    card.append(i)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])