import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    operation = input()
    if "push_front" in operation:
        q.insert(0, int(operation.split()[1]))
    elif "push_back" in operation:
        q.append(int(operation.split()[1]))
    elif "pop_front" in operation:
        print(q.popleft()) if q else print(-1)
    elif "pop_back" in operation:
        print(q.pop()) if q else print(-1)

    elif "size" in operation:
        print(len(q))
    elif "empty" in operation:
        if not q:
            print(1)
        else:
            print(0)
    elif "front" in operation:
        print(q[0]) if q else print(-1)
    elif "back" in operation:
        print(q[-1]) if q else print(-1)
