import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
answer = 0

# itertools를 활용한 풀이 132ms
for i in range(2, N+1):
    for com in combinations(A, i):
        if L <= sum(com) <= R and com[-1] - com[0] >= X:
            answer += 1

print(answer)

# 재귀 함수를 통해 조합을 사용한 풀이 380ms
def dfs(i, path, begin):
    global answer

    if len(path) == i:
        # print(*path)
        tmp = 0
        for p in path:
            tmp += A[p]

        if L <= tmp <= R and A[path[-1]] - A[path[0]] >= X:
            answer += 1

        return

    for j in range(begin, N):
        if not visit[j]:
            visit[j] = True
            dfs(i, path + [j], j+1)
            visit[j] = False

for i in range(2, N+1):
    visit = [False] * (N+1)
    dfs(i, [], 0)

print(answer)