'''
* 아이디어 1
  - start부터 x만큼 반복적으로 sum 함수를 쓰게 되면 시간초과가 발생한다.
  - 따라서, 투 포인터를 활용하여 첫 지점에서만 sum을 활용하고
  - 나머지 지점에서는 start부분을 제거, end부분을 추가를 반복한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, x = map(int, input().split())
visit = list(map(int, input().split()))

max_value = 0
count = 0
end = x
interval_sum = 0
for start in range(n-x+1):

    if start == 0:
        interval_sum = sum(visit[:x])
    else:
        interval_sum += visit[end-1]

    if interval_sum > max_value:
        max_value = interval_sum
        count = 1
    elif interval_sum == max_value:
        count += 1

    end += 1
    interval_sum -= visit[start]

if max_value == 0:
    print("SAD")
else:
    print(max_value)
    print(count)