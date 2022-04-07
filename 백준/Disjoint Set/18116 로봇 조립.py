'''
* 체감 난이도 : ****

* 아이디어 1
  - union-find 알고리즘을 사용하면된다.
  - 단, 해당 집합의 크기를 매번 계산하게 되면 시간초과가 발생하기 때문에, union과정에서 집합의 크기를 관리해야한다.
  - 따라서, union 수행 시, a의 parent를 b로 바꾼다면, a의 집합사이즈를 b로 넘겨주고, a의 집합사이즈는 0으로 초기화한다.
  - 또한, 부모가 서로 같은 경우는 pass해야 정답이 된다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
        set_size[a] += set_size[b]
        set_size[b] = 0
    elif a > b:
        parent[a] = b
        set_size[b] += set_size[a]
        set_size[a] = 0
    else:
        pass

parent = [i for i in range(10**6 + 1)]
set_size = [1 for i in range(10**6 + 1)]


for _ in range(n):
    query = list(map(str, input().split()))
    if "I" in query:
        a, b = int(query[1]), int(query[2])
        union_parent(a, b)

    elif "Q" in query:
        c = int(query[1])
        p = find_parent(c)
        print(set_size[p])

