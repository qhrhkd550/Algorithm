'''
* 아이디어 1
  - A -> B, B -> C 이면 A -> C이므로 플로이드 와샬 알고리즘을 사용한다.
  - 주의할 점은 처음에 입력받을 때, 같은 명제가 주어질 수 있기 때문에
  - if not data[pre-65][post-65]: 해당 조건을 만족할 때만 값을 1로바꾸고 count를 1 증가시킨다.
  - 같은 입력이 주어지지 않으면 count에서 증가하지 않기 때문에 위 조건이 필요 없다.
  - 플로이드 와샬에서는 현재 직접적으로 갈 수 없는 곳이지만 하나를 공유해서 갈 수 있다면 명제를 참으로 만들어준다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque, defaultdict

n = int(input())
data = [[0] * 58 for _ in range(58)]
count = 0
for _ in range(n):
    h = input()
    pre, post = map(ord, h.split(" => "))
    if pre == post:
        continue
    if not data[pre-65][post-65]:
        data[pre-65][post-65] = 1
        count += 1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i != j and not data[i][j] and data[i][k] and data[k][j]:
                data[i][j] = 1
                count += 1

print(count)
for i in range(58):
    for j in range(58):
        if data[i][j] == 1:
            print(chr(i+65) + " => " + chr(j+65))