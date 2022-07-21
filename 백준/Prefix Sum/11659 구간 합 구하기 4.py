import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
data = list(map(int, input().split()))

prefix = [0]
tmp = 0
for i in data:
    tmp += i
    prefix.append(tmp)

for _ in range(m):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a-1])