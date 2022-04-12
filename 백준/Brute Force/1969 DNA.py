'''
* 아이디어 1
  - 각 자리별로 가장 많이 나온 문자를 선택하면 된다.
  - 직접 비교할 수 있지만, zip과 Counter를 사용하면 손쉽게 해결된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import Counter

n, m = map(int, input().split())
DNA = []
for _ in range(n):
    DNA.append(input())

answer = ['', 0]
for d in zip(*DNA):
    count = Counter(d)
    count = sorted(count.items(), key = lambda x: (-x[1], x[0]))
    answer[0] += count[0][0]
    answer[1] += n - count[0][1]

print(answer[0])
print(answer[1])