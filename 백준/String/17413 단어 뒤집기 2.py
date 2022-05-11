'''
  * 아이디어 1
    - <가 등장할 경우, >가 나오기 전까지 answer에 계속 추가한다.
    - 알파벳이나 숫자일 경우, <가 나오기 전까지 answer에 추가한다.
    - 공백인 경우, answer에 추가한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

S = input()
i = 0
answer = ''
while i < len(S):
    if S[i] == "<":
        while i < len(S) and S[i] != ">":
            answer += S[i]
            i += 1

    elif S[i].isalnum():
        tmp = ''
        while i < len(S) and S[i].isalnum():
            tmp += S[i]
            i += 1
        answer += tmp[::-1]

    else:
        answer += S[i]
        i += 1

print(answer)