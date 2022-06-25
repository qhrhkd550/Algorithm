'''
  * 아이디어 1
    - dp[i] : i까지 오는 최소 힘
    - dp[i] : j -> i로 갈때 드는 힘과 0 -> j까지 오는데 드는 힘(dp[j])중 더 큰 힘이다.

'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
dp = [float('inf')] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        power = max((i-j) * (1 + abs(data[i] - data[j])), dp[j])
        dp[i] = min(dp[i], power)

print(dp[-1])
