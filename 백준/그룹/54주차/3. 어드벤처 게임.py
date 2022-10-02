import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque, defaultdict


def bfs():
    while q:
        x, y = q.popleft()
        if x == n-1:
            return True

        for i in data[x][2]:
            i -= 1
            if data[i][0] == 'L':
                tmp = y
                if y < data[i][1]:
                    tmp = data[i][1]

                if not visit[i][tmp]:
                    visit[i][tmp] = True
                    q.append((i, tmp))

            elif data[i][0] == 'T':
                if y >= data[i][1] and not visit[i][y-data[i][1]]:
                    visit[i][y-data[i][1]] = True
                    q.append((i, y-data[i][1]))

            elif data[i][0] == 'E':
                if not visit[i][y]:
                    visit[i][y] = True
                    q.append((i, y))

    return False

while True:
    n = int(input())
    if n == 0:
        break

    data = defaultdict(lambda : ['', 0, []])
    q = deque()
    visit = [[False] * 501 for _ in range(1000)]
    for i in range(n):
        info = list(map(str, input().split()))
        if i == 0:
            if info[0] == 'L':
                visit[0][int(info[1])] = True
                q.append((0, int(info[1])))
            else:
                visit[0][0] = True
                q.append((0, 0))

        data[i][0] = info[0]
        data[i][1] = int(info[1])
        data[i][2] = list(map(int, info[2:-1]))

    if data[0][0] == 'T':
        print("No")
        continue

    if bfs():
        print("Yes")
    else:
        print("No")