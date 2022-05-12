import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
data = list(map(int, input().split()))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    data[i-1] %= 2
    for j in range(k+1):
        if data[i-1] == 0: #짝수일 때
            dp[i][j] = dp[i-1][j] + 1
        if j != 0 and data[i-1]: #홀수일 때 
            dp[i][j] = dp[i-1][j-1]
            
answer = 0
for i in dp:
    if answer < i[k]:
        answer = i[k]
print(answer)
