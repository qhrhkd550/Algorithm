import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 0, max(tree)
answer = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for t in tree:
        if t > mid:
            tmp += t - mid
    if tmp == m:
        answer = mid
        break
    elif tmp > m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
