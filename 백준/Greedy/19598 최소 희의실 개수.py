import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

n = int(input())
data = []
for _ in range(n):
    start, end = map(int, input().split())
    data.append([start, end])
data.sort()

q = []
for start, end in data:
    if q and q[0] <= start:
        heapq.heappop(q)
    heapq.heappush(q, end)

print(len(q))