import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import Counter

t = int(input())
for _ in range(t):
    data = []
    answer = 1
    n = int(input())
    for _ in range(n):
        name, type = map(str, input().split())
        data.append([name, type])

    counter = Counter([key for value, key in data])

    for i in counter.values():
        answer *= (i+1)
    answer -= 1

    print(answer)
