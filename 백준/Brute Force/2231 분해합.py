'''
* 체감 난이도 : *

* 아이디어 1
  - 1부터 n-1까지 분해합 여부를 확인한다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
flag = False
for i in range(1, n):
    string_i = list(map(int, list(str(i))))
    if i + sum(string_i) == n:
        print(i)
        flag = True
        break

if not flag:
    print(0)