'''
  * 아이디어 1
    - 문제에서 주어진 조건대로 구현하면 되지만, 나뉘어질때 각 방향으로 이동하는 것이 아니라, 합쳐진 좌표에서 4개의 구슬이 생긴다는 점을 주의해야한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

n, m_, k = map(int, input().split())
data = defaultdict(list)
for _ in range(m_):
    r, c, m, s, d = map(int, input().split())
    data[(r-1, c-1)].append((m, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    tmp = defaultdict(list)
    for key, value in data.items():
        for m, s, d in value:
            nx = (key[0] + dx[d]*s) % n
            ny = (key[1] + dy[d]*s) % n
            tmp[(nx, ny)].append((m, s, d))

    remove_ = []
    new = []
    for key, value in tmp.items():
        length = len(value)
        if length >= 2:
            tmp_m, tmp_s, tmp_d = 0, 0, []

            for m, s, d in value:
                tmp_m += m
                tmp_s += s
                tmp_d.append(d)
                remove_.append((key[0], key[1], m, s, d))


            d_ = []
            if tmp_d[0] % 2 == 0:
                now_d = 'even'
            else:
                now_d = 'odd'
            flag = True
            for d_ in tmp_d[1:]:
                if (d_ % 2 == 0 and now_d == 'odd') or (d_ % 2 != 0 and now_d == 'even'):
                    flag = False
                    break
            if flag:
                d_ = [0, 2, 4, 6]
            else:
                d_ = [1, 3, 5, 7]

            tmp_m //= 5
            tmp_s //= length
            if tmp_m != 0:
                for i in range(4):
                    new.append((key[0], key[1], tmp_m, tmp_s, d_[i]))

    for x, y, m, s, d in remove_:
        tmp[(x, y)].remove((m, s, d))
        if len(tmp[(x, y)]) == 0:
            del tmp[(x, y)]

    for x, y, m, s, d in new:
        tmp[(x, y)].append((m, s, d))
    data = tmp

answer = 0
for key, value in data.items():
    for v in value:
        answer += v[0]

print(answer)