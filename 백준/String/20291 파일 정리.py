import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

n = int(input())
data = defaultdict(int)
for _ in range(n):
    file = input()
    data[file.split('.')[1]] += 1

data = sorted(data.items(), key=lambda x : x[0])
for a, b in data:
    print(a, b)
