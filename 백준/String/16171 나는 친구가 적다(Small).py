'''
  * 아이디어 1
    - 정규식을 사용해 숫자를 모두 공백으로 치환한다.
    - 치환한 문자열에 find가 존재하면 1, 아니면 0
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
import re

S = input()
find = input()

S = re.sub(r'[0-9]+', '', S)

if find in S:
    print(1)
else:
    print(0)