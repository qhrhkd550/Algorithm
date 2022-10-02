import sys

input = lambda: sys.stdin.readline().rstrip()

N, M, T, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(T)]

x, y, answer = 0, 0, 0


def check(x, y):
    tmp_count = 0

    # tmp = [[d1, d2] for d1, d2 in data if i <= d1 <= i + K and j - K <= d2 <= j]
    for d1, d2 in data:
        if x <= d1 <= x + K and y <= d2 <= y + K:
            tmp_count += 1

    return tmp_count


for i in range(T):
    for j in range(T):
        xx, yy = 0, 0
        if data[i][0] + K > N:
            xx = N - K
        else:
            xx = data[i][0]

        if data[j][1] + K > M:
            yy = M - K
        else:
            yy = data[j][1]

        count = check(xx, yy)
        if count > answer:
            x, y = xx, yy + K
            answer = count


print(x, y)
print(answer)
