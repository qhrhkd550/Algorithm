'''
  * 아이디어 1
    - B를 2로 나눌 수 있으면 2로 나눈다.
    - B를 2로 나눌 수 없고, B의 마지막 숫자가 1이라면 1을 제거한다.
    - 이때, B가 A보다 작다면 만들 수 없는 경우이다.
    - 만약 위의 경우에 해당하지 않는다면 A를 2배하거나 1을 붙여서 만들 수 없는 수이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

A, B = map(int, input().split())
answer = 0

while True:
    if A == B:
        print(answer + 1)
        break

    if B % 2 == 0:
        B //= 2
        answer += 1

    elif str(B)[-1] == "1":
        B = int(str(B)[:-1])
        answer += 1
        if A > B:
            print(-1)
            break

    else:
        print(-1)
        break