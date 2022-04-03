'''
* 체감 난이도 : *

* 아이디어 1
  - 한 문장씩 입력받아, [::-1] 을 활용하여 문자열을 뒤집는다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    string = input()
    if string == "END":
        break

    print(string[::-1])