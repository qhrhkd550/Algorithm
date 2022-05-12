'''
  * 아이디어 1
    - bag[i][j] = max(현재 물건 가치 + bag[이전 물건][현재 가방 무게 - 현재 물건 무게], bag[이전 물건][현재 가방 무게])
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
data = [[0, 0]]
for _ in range(n):
    data.append(list(map(int, input().split())))

bag = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = data[i][0]
        value = data[i][1]

        if j < weight:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j-weight] + value, bag[i-1][j])
print(bag[n][k])