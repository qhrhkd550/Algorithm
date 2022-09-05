import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + data[i-1][j-1]

answer = prefix[1][1]

for size in range(n):
    for i in range(1, n+1-size):
        for j in range(1, n+1-size):
            profit = prefix[i+size][j+size] - prefix[i-1][j+size] - prefix[i+size][j-1] + prefix[i-1][j-1]
            answer = max(answer, profit)

print(answer)