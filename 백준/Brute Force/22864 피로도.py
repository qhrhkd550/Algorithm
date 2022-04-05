'''
* 체감 난이도 : **

* 아이디어 1
  - 24시간만 확인하면 되므로 for문을 통해 해결
  - 주의할 점은 피로도가 음수가 되었을때 0으로 만들어야한다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

a, b, c, m = map(int, input().split())
answer = 0
total = 0
if a > m:
    print(0)
else:
    for i in range(24):
        if total + a <= m:
            total += a
            answer += b
        else:
            total -= c
            if total < 0:
                total = 0

    print(answer)