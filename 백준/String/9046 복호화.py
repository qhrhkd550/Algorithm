'''
* 체감 난이도 : *

* 아이디어 1
  - 입력받은 문자열의 공백을 제거 후
  - Counter 모듈을 사용해 알파벳 개수를 체크
  - 사용한 알파벳 순서대로 내림차순 정렬 후 최대값이 여러개라면 ? 출력, 그렇지 않은 경우 해당 key 출력

* 주의!
  - count = sorted(count.items(), key=lambda x:x[1], reverse=True) 를 사용하면 되지만,
  - count = sorted(count.items(), key=lambda x:-x[1]) 를 사용하면 "틀렸습니다" 결과를 받는다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import Counter

t = int(input())
for _ in range(t):
    string = input().replace(" ", "")
    count = Counter(string)
    count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    key, value = count[0][0], count[0][1]

    if len(count) > 1 and value == count[1][1]:
        print("?")
    else:
        print(key)