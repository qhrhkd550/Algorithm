'''
* 체감 난이도 : ***

* 아이디어 1
  - 1부터 n까지 수의 합은 (n * (n+1)) / 2 를 사용한다.
  - 1부터 mid까지의 합이 s보다 크면, s 이상을 만들 수 있다는 뜻이므로 end를 줄이고
  - s보다 작다면, s를 만들 수 있으므로 answer에 저장 후 start를 늘린다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

s = int(input())
start, end = 0, s
answer = 0
while start <= end:
    mid = (start + end) // 2
    tmp = (mid * (mid+1)) // 2
    if tmp > s:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)