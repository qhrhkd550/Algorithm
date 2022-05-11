'''
  * 아이디어 1
    - 회문이라면 바로 0을 출력하면된다.
    - 회문이 아니라면 유사회문인지 검사해야한다. 이때, 투포인터를 사용한다.
    - data[left]와 data[right]가 다를 경우, left + 1, right - 1중 선택해야 한다.
    - 한번 선택하고나면 두 포인터가 가리키는 값이 다른 경우, 유사회문이 아니라 판단하면된다.
    - 따라서 삭제 후 회문인지를 판단하는 함수를 left + 1, right - 1에 대해 각각 수행한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

def ispseudo(data, left, right): # 한 문자를 제거한 상태이기 때문에 두 포인터가 가리키는 값이 다르다면 False
    while left < right:
        if data[left] != data[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


def ispalindrome(data, left, right):
    if data == data[::-1]: # 회문이라면 0 리턴
        return 0
    else:
        while left < right:
            if data[left] != data[right]: # 두 문자가 다르다면 각각의 경우에 대해 각각 검사한다.
                check_left = ispseudo(data, left + 1, right)
                check_right = ispseudo(data, left, right - 1)

                if check_left or check_right: # 두 경우 중, 하나라도 유사회문이면 1 리턴
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

for _ in range(t):
    data = input()
    left, right = 0, len(data) - 1
    answer = ispalindrome(data, left, right)
    print(answer)


