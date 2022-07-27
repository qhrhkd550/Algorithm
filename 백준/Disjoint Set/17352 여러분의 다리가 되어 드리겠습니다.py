'''
  * 아이디어 1
    - union find를 사용하면 된다.
    - 주의할 점은 모든 간선에 대해 union_parent 함수를 호출한 후, 모든 노드에 대해 다시한번 부모를 찾아야한다.
    - 그렇지 않으면 parent의 값이 루트부모값이 아닌, 바로 위의 부모 값을 가리키고 있을 수 있기 때문이다 (31, 32 line)
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)]

for _ in range(n-2):
    a, b = map(int, input().split())
    union_parent(a, b, parent)

for i in range(1, n+1):
    parent[i] = find_parent(i, parent)

tmp = list(set(parent[1:]))
print(tmp[0], tmp[1])
