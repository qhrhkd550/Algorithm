'''
* 체감 난이도 : *

* 아이디어 1
  - deque를 사용하여 양방향 입출력이 가능한 큐 구현
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    operation = input()
    if "push" in operation:
        q.append(int(operation.split()[1]))
    elif "pop" in operation:
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif "size" in operation:
        print(len(q))
    elif "empty" in operation:
        if not q:
            print(1)
        else:
            print(0)
    elif "front" in operation:
        if not q:
            print(-1)
        else:
            print(q[0])
    elif "back" in operation:
        if not q:
            print(-1)
        else:
            print(q[-1])