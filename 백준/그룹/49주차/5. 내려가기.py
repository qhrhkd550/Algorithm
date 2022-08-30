import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    tmp = list(map(int, input().split()))

    for j in range(3):
        if j == 0:
            max_tmp[j] = max(max_dp[j], max_dp[j+1]) + tmp[j]
            min_tmp[j] = min(min_dp[j], min_dp[j + 1]) + tmp[j]

        elif j == 2:
            max_tmp[j] = max(max_dp[j], max_dp[j - 1]) + tmp[j]
            min_tmp[j] = min(min_dp[j], min_dp[j - 1]) + tmp[j]

        else:
            max_tmp[j] = max(max_dp[j], max_dp[j - 1], max_dp[j + 1]) + tmp[j]
            min_tmp[j] = min(min_dp[j], min_dp[j - 1], min_dp[j + 1]) + tmp[j]

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_tmp), min(min_tmp))