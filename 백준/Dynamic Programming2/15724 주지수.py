'''
  * 아이디어 1
    - 누적합을 이용하는 문제이다.
    - 누적합을 위해서 테두리에 0을 추가하고 공식에따라 구현하면된다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

data = [[0] * (m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]


for i in range(1, n+1):
    for j in range(2, m+1):
        data[i][j] += data[i][j-1]

for j in range(1, m+1):
    for i in range(2, n+1):
        data[i][j] += data[i-1][j]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    answer = data[x2][y2] - data[x2][y1-1] - data[x1-1][y2] + data[x1-1][y1-1]
    print(answer)