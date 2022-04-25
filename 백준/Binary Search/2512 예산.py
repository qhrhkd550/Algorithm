'''
  * 아이디어 1
    - 금액의 합이 m 보다 작거나 같은 최대값을 구하면 된다.
    - 따라서, tmp <= m이라면 더 큰 범위에서 찾아보고 반대의 경우 더 작은 범위에서 찾아본다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
m = int(input())

start, end = 0, max(data)
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for d in data:
        if d >= mid:
            tmp += mid
        else:
            tmp += d

    if tmp <= m:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)

