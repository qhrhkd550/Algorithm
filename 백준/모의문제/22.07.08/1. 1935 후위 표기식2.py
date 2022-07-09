import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
post = input()
num = [int(input()) for _ in range(n)]
index = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
stack = []
for p in post:
    if p.isalpha():
        stack.append(num[index.find(p)])
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(float(eval(str(num2) + p + str(num1))))

print("{:.2f}".format(stack[-1]))