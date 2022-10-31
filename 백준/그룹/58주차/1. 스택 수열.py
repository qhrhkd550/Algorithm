import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
stack = []
answer = []
top = 1
for _ in range(n):
    num = int(input())
    if not stack or stack[-1] < num:
        for i in range(top, num+1):
            stack.append(i)
            answer.append('+')

        stack.pop()
        answer.append('-')
        top = num + 1

    elif stack[-1] == num:
        stack.pop()
        answer.append('-')
        # top -= 1

    else:
        answer = ['NO']
        break

for a in answer:
    print(a)