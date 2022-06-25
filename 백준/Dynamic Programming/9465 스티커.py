'''
  * 아이디어 1
    - 50 10 100 20 40
      30 50 70  10 60 일때, 인덱스 1부터 보면
      인덱스가 1일때는 첫번째 행은 왼쪽 아래 대각선방향과 더하면 된다. 두번째 행은 왼쪽 위 대각선과 더하면 된다.
      인덱스가 2 이상일때는 첫번째 행은 왼쪽 아래 대각선 두칸을 보면되고, 두번째행은 왼쪽 위 대각선 두칸을 보고 큰 값과 더하면된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(t):
    answer = 0
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]

    for i in range(1, n):
        if i == 1:
            data[0][i] += data[1][i-1]
            data[1][i] += data[0][i-1]
        else:
            data[0][i] += max(data[1][i-1], data[1][i-2])
            data[1][i] += max(data[0][i - 1], data[0][i - 2])

    print(max(data[0][n-1], data[1][n-1]))