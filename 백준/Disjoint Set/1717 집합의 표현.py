'''
* 체감 난이도 : ***

* 아이디어 1
  - union-find 알고리즘을 사용하면된다.
  - 0일경우, 두 노드를 union 시키고, 1일경우, 두 노드의 부모가 같다면 YES, 다르면 NO를 출력시킨다.
  - 단, setrecursionlimit가 100,000을 넘을 경우 메모리초과가 발생하고
  - union_parent, find_parent 함수에 parent를 넘겨줄 경우 메모리 초과가 발생한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

parent = [i for i in range(n+1)]

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(a, b)
    elif oper == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
