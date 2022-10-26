import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
data = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    A, B = map(int, input().split())
    data[A][B] = 1
    data[B][A] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                data[i][j] = min(data[i][j], data[i][k] + data[k][j])

answer = 0
value = float('inf')
for i in range(1, n+1):
    tmp = sum(list(map(lambda x : 0 if x == float('inf') else x, data[i])))
    if value > tmp:
        value = tmp
        answer = i

print(answer)