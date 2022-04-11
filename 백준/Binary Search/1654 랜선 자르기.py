import sys
input = lambda : sys.stdin.readline().rstrip()

k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

def binary_search(start, end):

    if start > end:
        return end

    mid = (start + end) // 2
    tmp = 0
    for l in lan:
        tmp += l//mid

    if tmp >= n:
        return binary_search(mid+1, end)
    else:
        return binary_search(start, mid-1)

print(binary_search(1, max(lan)))