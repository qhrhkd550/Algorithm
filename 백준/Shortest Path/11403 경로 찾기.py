'''
* 체감 난이도 : **

* 아이디어 1
  - 플로이드 와샬을 사용해 i에서 j로 가는 경로가 바로 있다면 data[i][j] = 1
  - i에서 j로 가는 경로가 바로 없다면, data[i][k] == 1, data[k][j] == 1이라면 k를 거쳐서 갈 수 있다는 뜻이므로 data[i][j] = 1
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1 or (data[i][k] == 1 and data[k][j] == 1):
                data[i][j] = 1
            else:
                data[i][j] = 0

for i in range(n):
    for j in range(n):
        print(data[i][j], end=' ')
    print()