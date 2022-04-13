'''
* 체감 난이도 : ****

* 아이디어 1
  - 미세먼지 확산
    - 모든 미세먼지를 한번에 확산시켜야하기 때문에 확산되는 곳을 딕셔너리로 관리하여 값을 누적하였다.
    - 딕셔너리의 값을 원래 데이터 배열에 추가시킨다.
  - 청정기 순환
    - 위쪽, 아래쪽만 구분 잘하면 크게 문제없다.

* 주의
  - 미세먼지를 확신시킬때, 값 누적을 딕셔너리로 관리하면 시간이 1936ms
  - 미세먼지를 확산시킬때, 값 누적을 2차원배열로 관리하면 시간이 496ms 이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque, defaultdict

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(r)]

for _ in range(t):
    # 미세먼지 확산
    q = deque()
    for i in range(r):
        for j in range(c):
            if data[i][j] > 0:
                q.append((i, j))

    plus = defaultdict(int)
    # tmp = [[0] * c for _ in range(r)]
    for x, y in q:
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if data[nx][ny] == -1:
                continue

            plus[(nx, ny)] += data[x][y] // 5
            # tmp[nx][ny] += data[x][y] // 5
            count += 1

        data[x][y] -= (data[x][y]//5) * count

    for key, value in plus.items():
        i, j = key
        data[i][j] += value

    # for i in range(r):
    #     for j in range(c):
    #         data[i][j] += tmp[i][j]

    # 공기청정기 작동
    def right(x1, y1, x2, y2):
        for i in range(x1+1, x2):
            data[i][y1] = data[i + 1][y1]

        for i in range(y1, y2):
            data[x2][i] = data[x2][i + 1]

        for i in range(x2, x1, -1):
            data[i][y2] = data[i - 1][y2]

        for i in range(y2, y1, -1):
            if i == y1 + 1:
                data[x1][i] = 0
            else:
                data[x1][i] = data[x1][i - 1]

    def left(x1, y1, x2, y2):
        for i in range(x1-1, x2, -1):
            data[i][y1] = data[i-1][y1]

        for i in range(y1, y2):
            data[x2][i] = data[x2][i+1]

        for i in range(x2, x1):
            data[i][y2] = data[i+1][y2]

        for i in range(y2, y1, -1):
            if i == y1 + 1:
                data[x1][i] = 0
            else:
                data[x1][i] = data[x1][i-1]

    clear = []
    for i in range(r):
        for j in range(c):
            if data[i][j] == -1:
                clear.append((i, j))

    left(clear[0][0], clear[0][1], 0, c-1)
    right(clear[1][0], clear[1][1], r-1, c-1)

answer = 2
for d in data:
    answer += sum(d)
print(answer)