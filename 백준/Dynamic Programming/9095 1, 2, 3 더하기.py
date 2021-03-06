import sys
input = lambda : sys.stdin.readline().rstrip()


T = int(input())
n = []
for _ in range(T):
    n.append(int(input()))

dp = [0] * (max(n)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, max(n)+1):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in n:
    print(dp[i])