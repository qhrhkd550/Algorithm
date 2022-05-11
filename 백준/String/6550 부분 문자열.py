'''
  * 아이디어 1
    - s와 t의 문자가 같다면 두 인덱스를 모두 증가시키고, 다르다면 t의 인덱스만 증가시킨다.
    - 최종적으로 s의 인덱스는 s의 길이보다 작지만, t의 인덱스는 t의 길이와 같은 경우, 부분 문자열이 아닌경우이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    try:
        s, t = map(str, input().split())
        i = 0  # s의 index
        j = 0  # t의 index
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i < len(s) and j == len(t):
            print("No")
        else:
            print("Yes")
    except:
        break
