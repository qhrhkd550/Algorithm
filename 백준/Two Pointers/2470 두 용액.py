'''
* 아이디어 1
  - 용액을 정렬한 후, 양끝에서부터 start와 end를 설정해 계산하면된다.
  - 계산된 용액의 합이 양수일 경우 end를 줄이면 되고, 음수인경우 start를 늘리면된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))

data.sort()
start = 0
end = n-1

min_value = float('inf')
answer = []

while start < end:
    mix = data[start] + data[end]
    if abs(mix) < min_value:
        min_value = abs(mix)
        answer = [data[start], data[end]]
        if min_value == 0:
            break

    if mix > 0:
        end -= 1
    else:
        start += 1

answer.sort()
for a in answer:
    print(a, end=' ')
