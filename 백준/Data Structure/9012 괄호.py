'''
* 체감 난이도 : *

* 아이디어 1
  - stack을 사용해 열린괄호만 stack에 삽입하고, 닫힌괄호를 만나면 stack.pop을 수행한다.
  - 만약, 마지막에 stack에 열린괄호가 있다면, return False
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

def check(string):
    for s in string:
        if not stack:
            if s == ")":
                return False
            stack.append(s)
        else:
            if s == ")":
                stack.pop(-1)
            else:
                stack.append(s)

    if stack:
        return False

    return True

for _ in range(t):
    string = input()
    stack = []
    if check(string):
        print("YES")
    else:
        print("NO")