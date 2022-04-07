'''
* 체감 난이도 : **

* 아이디어 1
  - union-find 알고리즘을 사용하여 연결되어 있는 노드들 간의 parent 정보를 생성한다.
  - 여행 순서가 A B C D 라면 A와 B의 부모가 같다면 연결되어있다는 상태이므로 A B, B C, C D 를 차례로 부모정보를 비교하여
  - 부모가 다른 쌍이 나오면 갈 수 없으므로 NO를 출력하고 종료한다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

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

parent = [i for i in range(n)]

data = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            union_parent(i, j)

route = list(map(int, input().split()))
flag = True
for i in range(m-1):
    if find_parent(route[i]-1) != find_parent(route[i+1]-1):
        print("NO")
        flag = False
        break
if flag:
    print("YES")