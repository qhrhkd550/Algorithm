'''
* 아이디어 1
  - ()를 만날때마다 현재 stack에 들어있는 (에 값을 1씩 추가해준다. 즉, 막대기가 레이저를 만나 분할된다는 뜻이다.
  - stack에 막대기를 추가할때는 (가 아니라 1을 넣는다. 즉, 막대기가 하나의 막대기란 뜻이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

string = input()

razer = 0
stack  = []
answer = 0
i = 0
while i < len(string)-1:
    if string[i] == "(":
        if string[i+1] == ")":
            for j in range(len(stack)):
                stack[j] += 1
            i += 1
        else:
            stack.append(1)

    else:
        answer += stack.pop()

    i += 1

if stack:
    answer += stack[-1]
print(answer)