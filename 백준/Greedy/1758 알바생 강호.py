'''
  * 아이디어 1
    - 팁을 받는 수식이 정해져있기 때문에 팁을 많이 주는 사람부터 입장시켜야
    - 강호가 가장 많은 팁을 받을 수 있다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
customer = []
for _ in range(n):
    customer.append(int(input()))

customer.sort(reverse=True)

answer = 0
for i in range(n):
    tip = customer[i] - (i+1 - 1)
    if tip >= 0:
        answer += tip

print(answer)