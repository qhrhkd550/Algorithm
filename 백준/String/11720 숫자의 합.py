'''
* 체감 난이도 : *

* 아이디어 1
  - sum 함수 이용
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input()))

print(sum(data))