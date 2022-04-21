'''
* 아이디어 1
  - 모든 지점을 살펴보고 최대 아이템 수를 가져야 하므로, 다익스트라보다는 플로이드와샬이 효율적이다.
  - 우선 플로이드와샬을 통해 각 지점에서 각 지점으로의 최단 거리를 구한다.
  - 각 지점에서 m보다 작은 거리에 있는 지점들의 item 합을 구하고
  - 각 지점 item 합의 최대를 구한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
map_ = [[float('inf')] * n for _ in range(n)]
for _ in range(r):
    a, b, i = map(int, input().split())
    map_[a-1][b-1] = i
    map_[b-1][a-1] = i

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                map_[i][j] = min(map_[i][j], map_[i][k] + map_[k][j])

answer = 0
for i in range(n):
    tmp = item[i]
    for j in range(n):
        if i != j:
            if map_[i][j] <= m:
                tmp += item[j]
                
    if answer < tmp:
        answer = tmp

print(answer)


        
