import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
k = int(input())
data = []
for _ in range(k):
    data.append(list(map(int, input().split())))
data.sort()
dp = [[0] * (t+1) for _ in range(k+1)]
for i in range(k+1):
    dp[i][0] = 1

for i in range(1, k+1):
    for num in range(data[i][1] + 1):
        for j in range(t+1):
