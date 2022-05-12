import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
dp = [[0] * n for _ in range(k)]

for i in range(k):
    for j in range(n):
        if i == 0:
            dp[i][j] = 1

        if j == 0:
            dp[i][j] = i+1

        if i > 0 and j > 0:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[k-1][n-1] % 1000000000)