import sys
input = lambda : sys.stdin.readline().rstrip()

n, k, q, m = map(int, input().split())

sleep = [0] * (n+3)
check = [0] * (n+3)

sleep_stu = list(map(int, input().split()))
for stu in sleep_stu:
    sleep[stu] = 1

q_stu = list(map(int, input().split()))
for stu in q_stu:
    if sleep[stu] == 1:
        continue
    for j in range(stu, n+3, stu):
        if not sleep[j]:
            check[j] = 1

prefix = [0]
for i in range(1, n+3):
    prefix.append(prefix[-1] + check[i])

for _ in range(m):
    s, e = map(int, input().split())
    print(e-s+1 - (prefix[e]-prefix[s-1]))

