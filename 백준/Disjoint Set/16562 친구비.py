'''
  * 아이디어 1
    - 친구의 친구는 친구이기 때문에, 유니온파인드 알고리즘을 사용한다.
    - 모든 친구관계에 대해 유니온파인드를 적용 후, 부모를 통일시키기 위해 find알고리즘을 한번 더 적용한다.
    - 부모 노드들의 A 값만 가져오고, 그 합이 가진 돈보다 작다면 출력, 아니라면 Oh no를 출력한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if A[a] < A[b]:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    v, w = map(int, input().split())
    union_parent(v, w)

for i in range(1, n+1):
    parent[i] = find_parent(i)

friend = set(parent[1:])
answer = 0
for f in friend:
    answer += A[f]

if answer > k:
    print("Oh no")
else:
    print(answer)
