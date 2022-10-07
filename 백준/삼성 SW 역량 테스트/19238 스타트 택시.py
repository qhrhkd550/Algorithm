import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m, fuel = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
taxi_x, taxi_y = map(lambda x : x-1, map(int, input().split()))
passenger_start = []
passenger_end = []
for _ in range(m):
    sx, sy, ex, ey = map(lambda x : x-1, map(int, input().split()))
    passenger_start.append((sx, sy))
    passenger_end.append((ex, ey))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def find_passenger(x, y):
    global fuel
    q = deque()
    q.append((x, y))
    taxi_distance[x][y] = 0
    while q:
        x, y = q.popleft()

        if (x, y) in passenger_start:
            if fuel < taxi_distance[x][y]:
                return False
            index = passenger_start.index((x, y))
            sub = passenger_start.pop(index)
            fuel -= taxi_distance[x][y]
            return (index, sub)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if taxi_distance[nx][ny] > -1 or data[nx][ny] == 1:
                continue

            taxi_distance[nx][ny] = taxi_distance[x][y] + 1
            q.append((nx, ny))
    return False
#
def find_destination(index, sub):
    global fuel
    q = deque()
    q.append(sub)
    visit[sub[0]][sub[1]] = 0

    while q:
        x, y = q.popleft()
        if (x, y) == passenger_end[index]:
            # print(x, y, fuel, visit[x][y])
            if fuel < visit[x][y]:
                return -1, -1
            fuel -= visit[x][y]
            fuel += (visit[x][y]) * 2
            passenger_end.remove((x, y))
            return x, y

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visit[nx][ny] > -1 or data[nx][ny] == 1:
                continue

            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))

    return -1, -1

flag = True
while passenger_end:
    taxi_distance = [[-1] * n for _ in range(n)]
    result = find_passenger(taxi_x, taxi_y)
    # print(result)
    visit = [[-1] * n for _ in range(n)]
    if result:
        taxi_x, taxi_y = find_destination(result[0], result[1])
        # print(taxi_x, taxi_y)
        if taxi_x == -1 and taxi_y == -1:
            flag = False
            print(-1)
            break
    else:
        flag = False
        print(-1)
        break
    # print("한번", fuel, taxi_x, taxi_y)

if flag:
    print(fuel)