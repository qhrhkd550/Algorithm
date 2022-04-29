import sys
input = lambda : sys.stdin.readline().rstrip()


dp = [0] * 1001
dp[0] = 1
dp[1] = 1
dp[2] = 3
for i in range(3, 1001):
    dp[i] = (dp[i-2] * 2 + dp[i-1]) % 10007

n = int(input())
print(dp[n] % 10007)