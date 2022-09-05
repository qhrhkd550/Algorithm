import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijstrak(x, y):
    q = []
    heapq.heappush(q, (x, y, data[0][0]))
    distance[0][0] = 0

    while q:
        x, y, cost = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if distance[nx][ny] < cost:
                continue

            if distance[nx][ny] > cost + data[nx][ny]:
                distance[nx][ny] = cost + data[nx][ny]
                heapq.heappush(q, (nx, ny, cost + data[nx][ny]))


i = 1
while True:
    n = int(input())
    if n == 0:
        break
    data = [list(map(int, input().split())) for _ in range(n)]
    distance = [[float('inf')] * n for _ in range(n)]
    dijstrak(0, 0)

    print("Problem " + str(i) + ": " + str(distance[n-1][n-1]))
    i += 1
