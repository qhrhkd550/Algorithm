import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    answer = 1
    item = defaultdict(list)

    for _ in range(n):
        name, type = input().split()
        item[type].append(name)

    for key, value in item.items():
        answer *= len(value) + 1

    print(answer - 1)