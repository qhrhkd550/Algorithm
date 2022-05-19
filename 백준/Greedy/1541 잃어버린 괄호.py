'''
  * 아이디어 1
    - 정규식을 사용해 연산자 기준으로 split한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
import re

string = input()

string = re.split(r"([+-])", string)
for i in range(len(string)):
    if string[i].isalnum():
        string[i] = str(int(string[i]))


while "+" in string:
    index = string.index("+")
    string.pop(index)
    num1 = int(string.pop(index-1))
    num2 = int(string.pop(index-1))
    string.insert(index-1, str(num1+num2))

print(eval(''.join(string)))