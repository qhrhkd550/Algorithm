'''
  * factorial을 매번 구하지 말고, dp배열로 구해놓으면 된다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

fact = [0] * (n+1)
fact[0] = 1
for i in range(1, n+1):
    fact[i] = fact[i-1] * i

print(fact[n] / (fact[m] * fact[n-m]))