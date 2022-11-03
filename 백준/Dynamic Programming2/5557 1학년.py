'''
  * 아이디어 1
    - dp[i][j] : i번째까지 수를 이용해서 j를 만들 수 있는 경우의 수
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]
dp[0][data[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:
            if 0 <= j + data[i] <= 20:
                dp[i][data[i] + j] += dp[i-1][j]
            if 0 <= j - data[i] <= 20:
                dp[i][j - data[i]] += dp[i-1][j]

print(dp[n-2][data[-1]])