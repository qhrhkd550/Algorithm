import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
location = []
for _ in range(n):
    heapq.heappush(location, list(map(int, input().split())))

L, P = map(int, input().split())

gas = []
count = 0
while P < L:
    while location and location[0][0] <= P: # 현재 기름으로 갈 수 있는 곳
        x, y = heapq.heappop(location)
        heapq.heappush(gas, [-y, x]) # 최대 충전을 해야하기 때문에 최대힙으로 사용

    if not gas:
        count = -1
        break

    y, x = heapq.heappop(gas)
    P -= y
    count += 1

print(count)

