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