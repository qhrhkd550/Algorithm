import sys
input = lambda : sys.stdin.readline().rstrip()

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())
for t in range(T):
    user_num = int(input())
    friend_num = int(input())

    parent = [i for i in range(user_num)]

    for _ in range(friend_num):
        a, b = map(int, input().split())
        union_parent(a, b)

    for i in range(user_num):
        parent[i] = find_parent(i)

    m = int(input())
    print(f"Scenario {t+1}:")
    for _ in range(m):
        u, v = map(int, input().split())
        if parent[u] == parent[v]:
            print(1)
        else:
            print(0)
    print()