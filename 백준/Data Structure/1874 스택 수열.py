import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
stack = []
now = 1
answer = []
for _ in range(n):
    num = int(input())
    if not stack or stack[-1] < num:
        for i in range(now, num+1):
            stack.append(i)
            answer.append("+")
        stack.pop()
        now = num+1
        answer.append("-")

    elif stack[-1] != num:
        answer = ["NO"]
        break

    else:
        stack.pop()
        answer.append("-")

for a in answer:
    print(a)