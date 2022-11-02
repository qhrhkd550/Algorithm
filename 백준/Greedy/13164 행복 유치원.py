import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
data = list(map(int, input().split()))

costs = []
for i in range(n-1):
    costs.append(data[i+1] - data[i])

costs.sort()
print(sum(costs[:n-k]))