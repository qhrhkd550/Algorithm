'''
* 아이디어 1
  - defaultdict를 사용해 각 숫자별로 몇개씩 나왔는지 체크한다.
  - 초기값이 0이기 때문에 k-1이하로 나올때까지 반복할 수 있다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

n, k = map(int, input().split())
data = list(map(int, input().split()))
end = 0
check = defaultdict(int)
max_length = 0
tmp = 0
for start in range(n):
    while end < n and check[data[end]] <= k-1:
        check[data[end]] += 1
        tmp += 1
        end += 1
    if max_length < tmp:
        max_length = tmp
    tmp -= 1
    check[data[start]] -= 1

print(max_length)