'''
  * 아이디어 1
    - 현재 문자에 대해서 처음 등장한 문자라면 딕셔너리에 True로 매핑시켜주고,
    - 현재 문자에 대해서 딕셔너리에 True라면 이미 방문했다는 뜻이므로 그룹 단어가 아니다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

n = int(input())
data = [input() for _ in range(n)]

answer = 0
for word in data:
    tmp = defaultdict(lambda : False)
    i = 0
    flag = True
    while i < len(word):
        now = word[i]
        if not tmp[now]:
            tmp[now] = True
            while i < len(word) and word[i] == now:
                i += 1

        elif tmp[now]:
            flag = False
            break

    if flag:
        answer += 1

print(answer)