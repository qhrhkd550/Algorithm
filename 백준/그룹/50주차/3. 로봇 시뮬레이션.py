import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

A, B = map(int, input().split())
N, M = map(int, input().split())

#     위  오  아  왼
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}

def change_direction(now_direction, rotate):
    if rotate == 'L':
        for _ in range(repeat):
            now_direction -= 1
            if now_direction < 0:
                now_direction = 3
    else:
        for _ in range(repeat):
            now_direction += 1
            if now_direction > 3:
                now_direction = 0

    return now_direction


def move_robot(n, x, y, d):
    for _ in range(repeat):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 1 or nx > A or ny < 1 or ny > B:
            return "Robot " + str(n) + " crashes into the wall"

        for key, value in data.items():
            if value[0] == nx and value[1] == ny:
                return "Robot " + str(n) + " crashes into robot " + str(key)

        x, y = nx, ny

    data[n][0], data[n][1] = x, y
    return "OK"

data = defaultdict()
number = 1
for _ in range(N):
    x, y, d = map(str, input().split())
    data[number] = [int(x), int(y), direction[d]]
    number += 1

flag = True
for _ in range(M):
    n, order, repeat = map(str, input().split())
    n = int(n)
    repeat = int(repeat)
    if order == 'F':
        result = move_robot(n, data[n][0], data[n][1], data[n][2])
        if result == "OK":
            continue
        print(result)
        flag = False
        break

    else:
        data[n][2] = change_direction(data[n][2], order)

if flag:
    print("OK")

