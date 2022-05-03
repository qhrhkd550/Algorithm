'''
  * 아이디어 1
    - 올바른 괄호를 판단하기 위해서는 stack 자료구조를 사용하면 간단하다.
    - 단, 점수를 더해야하기 때문에 아래와 같은 과정이 들어간다.
    - 열린 괄호를 만날 때 마다 해당 값을 임시값에 곱해준다.
    - 만약 닫힌 괄호를 만났을 때, 바로 전 괄호와 짝이 맞다면 지금까지 누적한 값을 정답에 더해주고
    - 만약 닫힌 괄호를 만났을 때, 바로 전 괄호와 짝이 맞지 않다면 이미 해당 값은 누적되고 있으므로 정답에 더해주지 않는다.
    - 닫힌괄호 후에는 임시 값을 괄호의 값에 따라 나눠주어야 한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

string = input()
stack = []

tmp, result = 1, 0
for i in range(len(string)):
    if string[i] == '(':
        tmp *= 2
        stack.append(string[i])

    elif string[i] == '[':
        tmp *= 3
        stack.append(string[i])

    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break

        if string[i-1] == '(':
            result += tmp
        tmp //= 2
        stack.pop()

    elif string[i] == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break

        if string[i-1] == '[':
            result += tmp
        tmp //= 3
        stack.pop()

if stack:
    result = 0
print(result)

