'''
* 아이디어 1
  - ()를 만날때마다 현재 stack에 들어있는 (에 값을 1씩 추가해준다. 즉, 막대기가 레이저를 만나 분할된다는 뜻이다.
  - stack에 막대기를 추가할때는 (가 아니라 1을 넣는다. 즉, 막대기가 하나의 막대기란 뜻이다.

* 풀이 1
  - ()를 만날때마다 현재 stack에 있는 개수만큼 추가한다.
  - ()가 아니라 그냥 )를 만났을 경우, 끄트머리 막대기를 의미하므로 +1 해준다.
  - 시간이 10배가까이 짧다.
  - 아래 주석코드 참고

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

# stack = []
# answer = 0
# for i in range(len(string)):
#     if string[i] == "(":
#         stack.append(string[i])
#     else:
#         if string[i-1] == "(":
#             stack.pop()
#             answer += len(stack)
# 
#         else:
#             stack.pop()
#             answer += 1
# 
# print(answer)
