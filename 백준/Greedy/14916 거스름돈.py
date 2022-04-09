import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
count = 0
while True:
    if n < 0:
        print(-1)
        break

    if n % 5 == 0:
        print(count + n // 5)
        break

    n -= 2
    count += 1