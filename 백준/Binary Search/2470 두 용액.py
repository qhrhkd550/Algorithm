'''
  * 아이디어 1
    - 가장 왼쪽과 오른쪽의 용액부터 시작하여 최소값을 업데이트 해나간다.
    - 만약 혼합용액의 값이 0보다 크다면 오른쪽(end)를 하나 줄이고, 0보다 작다면 왼쪽(start)를 하나 늘린다.
    - 혼합용액의 값이 0이라면 종료한다.
    - 같은 용액을 두 번 더하는건 안되므로 start < end 까지만 해야한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
data.sort()

start, end = 0, n-1
min_value = float('inf')
answer = [0, 0]
while start < end:
    mid = data[start] + data[end]
    if min_value > abs(mid):
        min_value = abs(mid)
        answer = [data[start], data[end]]

        if min_value == 0:
            break

    if mid > 0:
        end -= 1
    else:
        start += 1

print(*answer)
