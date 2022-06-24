'''
  * 아이디어 1
    - 이전까지의 최대값과 현재 자신의 값을 합쳤을 때 자신보다 크다면 이전까지 최대값 + 현재 자신의 값을 dp에 넣고,
    - 그렇지 않다면 현재 자신의 값을 dp에 넣는다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
dp = [-float('inf')] * n

dp[0] = data[0]
answer = dp[0]
for i in range(1, n):
    if data[i] < dp[i-1] + data[i]:
        dp[i] = dp[i-1] + data[i]
    else:
        dp[i] = data[i]

    if answer < dp[i]:
        answer = dp[i]

print(answer)