'''
* 체감 난이도 : *

* 아이디어 1
  - 파이썬에서는 list 자료구조가 stack이므로, list를 사용해 stack을 구현
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
stack = []
for _ in range(n):
    operation = input()
    if "push" in operation:
        stack.append(int(operation.split()[1]))
    elif "pop" in operation:
        if not stack:
            print(-1)
        else:
            print(stack.pop(-1))
    elif "size" in operation:
        print(len(stack))
    elif "empty" in operation:
        if not stack:
            print(1)
        else:
            print(0)
    elif "top" in operation:
        if not stack:
            print(-1)
        else:
            print(stack[-1])