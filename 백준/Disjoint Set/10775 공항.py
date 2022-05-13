'''
  * 아이디어 1
    - 도킹해야 할 게이트는 앞에서부터 탐색이 아니라 해당 번호에서 부터 탐색한다.
    - 즉, 게이트가 1 2 3 4 이고 gi가 4 1 1 일 때,
    - 4는 게이트4번에 도킹한다. 이때, 도킹했다는 의미로 4의 부모를 3으로 설정한다. (다음번에 4번에 도킹하고싶다면, 3번에 도킹하라는 의미이다.)
    - 위의 과정을 반복하되, 도킹하고자하는 번호가 0일경우, 더 이상 도킹못하는 경우이므로 종료한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

g = int(input())
p = int(input())
data = []
for _ in range(p):
    data.append(int(input()))


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(g+1)]

def result():
    answer = 0
    for d in data:
        pi = find_parent(d)
        if pi == 0:
            return answer

        else:
            union_parent(pi, pi-1)
            answer += 1
    return answer
answer = result()

print(answer)
