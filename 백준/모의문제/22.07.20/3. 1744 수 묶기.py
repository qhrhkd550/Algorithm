import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
minus = []
plus = []
total = []
answer = 0
for _ in range(n):
    a = int(input())
    if a <= 0:
        minus.append(a)
    elif a == 1:
        total.append(a)
    elif a > 0:
        plus.append(a)

minus.sort()
plus.sort(reverse=True)

while len(minus) > 1:
    a = minus.pop(0)
    b = minus.pop(0)
    total.append(a*b)

while len(plus) > 1:
    a = plus.pop(0)
    b = plus.pop(0)
    total.append(a*b)

answer = sum(total)
if minus:
    answer += sum(minus)
if plus:
    answer += sum(plus)

print(answer)

