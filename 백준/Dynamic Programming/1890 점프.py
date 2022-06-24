'''
  * 아이디어 1
    - 2차원 배열을 순서대로 방문하면서 0이 아닌 포인트에서만 아래작업을 수행한다.
    - 이동할 수 있다면 이동할 지점에 현재 위치의 dp값을 더한다. 이는 갈 수  있는 경로의 수를 더하는 것과 같다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            if i + data[i][j] < n:
                dp[i + data[i][j]][j] += dp[i][j]
            if j + data[i][j] < n:
                dp[i][j + data[i][j]] += dp[i][j]

print(dp[n-1][n-1])