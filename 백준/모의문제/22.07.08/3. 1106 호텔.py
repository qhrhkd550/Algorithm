import sys
input = lambda : sys.stdin.readline().rstrip()

C, N = map(int, input().split())
data = []
for _ in range(N):
    cost, customer = map(int, input().split())
    data.append((cost, customer))

dp = [float('inf')] * (C+100)
dp[0] = 0

data = sorted(data, key=lambda x : x[0])
for cost, customer in data:
    for i in range(customer, C+100):
        dp[i] = min(dp[i-customer] + cost, dp[i])

print(min(dp[C:]))