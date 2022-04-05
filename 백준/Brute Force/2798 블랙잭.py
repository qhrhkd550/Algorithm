'''
* 체감 난이도 : *

* 아이디어 1
  - 모든 카드 조합을 고려해야 하므로, combination 모듈을 사용해 합이 m을 넘지 않는 조합 중 최대를 출력한다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
answer = 0
for combination in combinations(card, 3):
    if sum(combination) <= m:
        answer = max(answer, sum(combination))

print(answer)