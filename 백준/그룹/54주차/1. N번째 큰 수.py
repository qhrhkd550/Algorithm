import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
q = []

for row in data:
    if not q:
        for r in row:
            heapq.heappush(q, r)
    else:
        for r in row:
            if q[0] < r:
                heapq.heappush(q, r)
                heapq.heappop(q)

print(q[0])
