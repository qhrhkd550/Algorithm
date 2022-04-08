import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dp = [i for i in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])