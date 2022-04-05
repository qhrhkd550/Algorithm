'''
* 체감 난이도 : *

* 아이디어 1
  - list에서 해당 인덱스를 제거하고, 인덱스는 %len(data)를 수행하여 리스트 범위를 벗어나지 않게 한다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
data = [i for i in range(1, n+1)]


answer = ''
i = 0
while data:
    i += k-1
    i %= len(data)
    answer += str(data.pop(i)) +", "

print("<" + answer[:-2] + ">")
