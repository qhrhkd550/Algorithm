import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

start, end = 0, n
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 >= n:
        end = mid - 1
    else:
        start = mid + 1

print(start)
