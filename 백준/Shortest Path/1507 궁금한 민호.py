'''
  - road : i에서 j로 가는 도로가 있으면 True, 초기에는 전부 True로 설정
  - i, j, k가 모두 다른 값이고 data[i][j] == data[i][k] + data[k][j] 이면 다른 도시를 거쳐서 왔다는 뜻이기 때문에 road[i][j] = False로 바꾼다.
  - 만약 i, j, k가 모두 다른 값이고 data[i][j] > data[i][k] + data[k][j]이면 최소값이 아니기 때문에 answer = -1
  - answer이 -1이 아닌 경우에만 존재하는 각 도로의 가중치를 더한다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
road = [[True] * n for _ in range(n)]

answer = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == k or j == k:
                continue
            if data[i][j] == data[i][k] + data[k][j]:
                road[i][j] = False
            elif data[i][j] > data[i][k] + data[k][j]:
                answer = -1

if answer != -1:
    for i in range(n):
        for j in range(i, n):
            if road[i][j]:
                answer += data[i][j]
print(answer)