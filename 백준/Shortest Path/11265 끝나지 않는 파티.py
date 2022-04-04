'''
* 체감 난이도 : *

* 아이디어 1
  - 플로이드 와샬을 사용해 모든 지점에서 모든지점까지 최단 거리를 구한다.
  - 최단거리가 곧 시간을 의미한다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

for _ in range(m):
    a, b, c = map(int, input().split())
    if data[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")