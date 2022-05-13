'''
  * 아이디어 1
    - 두 사람이 들어올 때마다 network에 몇명이 있는지 출력해야한다.
    - 만약 b가 a의 자식으로 들어갈 경우, b의 network 수를 a의 network수에 추가하고 b의 network 수는 0으로 만든다.
    - 유니온파인드 알고리즘은 서로다른 두 그룹이 생긴 후, 각 그룹의 루트들을 유니온 시키면 한 그룹의 자식들은 합쳐진 새로운 루트를 부모로 가지지 않는다.
    - 따라서, 모든 노드에 대해 다시 부모를 찾아야하는데, 이 문제의 경우 다시 부모를 찾으면 항상 같은 부모를 찾을 수 밖에 없다.
    - 또한, 이 문제의 경우 다시 부모를 찾으면 항상 같은 부모를 찾을 수 밖에 없기 때문에, 모든 노드에 대해 다시 부모를 찾을 필요없이 union할때마다 network값을 출력해도 무방하다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

t = int(input())

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        pass
        # print(network[a])
    else:
        if a < b:
            parent[b] = a
            network[a] += network[b]
            network[b] = 0
            # print(network[a])
        else:
            parent[a] = b
            network[b] += network[a]
            network[a] = 0
            # print(network[b])



for _ in range(t):
    f = int(input())
    parent = defaultdict(lambda: '')
    network = defaultdict(lambda: 1)
    for _ in range(f):
        a, b = map(str, input().split())
        if parent[a] == '':
            parent[a] = a

        if parent[b] == '':
            parent[b] = b

        union_parent(a, b)
        a = find_parent(a)
        b = find_parent(b)
        if a == b:
            print(network[a])