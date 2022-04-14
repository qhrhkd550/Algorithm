'''
* 팁
  - 소수 n 자리까지 출력 : "{:nf}".format(float)
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
postfix = input()
value = {}
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    value[alpha[i]] = input()
stack = []
for s in postfix:
    if s.isalpha():
        stack.append(value[s])
    else:
        p1 = stack.pop()
        p2 = stack.pop()
        tmp = eval(p2+s+p1)
        stack.append(str(tmp))

answer = "{:.2f}".format(float(stack[-1]))
print(answer)