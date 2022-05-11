'''
  * 아이디어 1
    - 시간을 고려하여 듣지못한 사람의 명단을 dict로 관리하고, 보지못한사람이 듣지못한사람의 dict에서 True일 경우, answer에 추가한다.

  * 아이디어 2
    - set을 사용하여 듣지못한사람의 set과 보지못한 사람의 set의 교집합을 구해도 된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

n, m = map(int, input().split())

listen = defaultdict(lambda : False)

for _ in range(n):
    listen[input()] = True

answer = []
for _ in range(m):
    see = input()
    if listen[see]:
        answer.append(see)

answer.sort()
print(len(answer))
for a in answer:
    print(a)