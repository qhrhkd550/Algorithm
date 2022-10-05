import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def find_island(x, y, island):
    q = deque()
    q.append((x, y))
    split_island[x][y] = island
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if split_island[nx][ny] or data[nx][ny] == 0:
                continue

            split_island[nx][ny] = island
            q.append((nx, ny))


def connect_bridge(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    start_island = split_island[x][y]
    end_island = 0
    while q:
        x, y = q.popleft()
        tmp_x, tmp_y = x, y
        for i in range(4):
            # print("i : ", i)
            count = 0
            x, y = tmp_x, tmp_y
            # i가 고정된 상태에서 끝까지 가야돼
            flag = True
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                # print(nx, ny)
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    # print("범위 아웃")
                    flag = False
                    break

                if split_island[nx][ny] == start_island:
                    # print("섬의 가장자리가 아니야")
                    visit[nx][ny] = True
                    count = 0
                    x, y = nx, ny
                    continue

                if split_island[nx][ny] == 0:
                    # print("바다 위 다리 연결 중")
                    x, y = nx, ny
                    count += 1

                if split_island[nx][ny] > 0 and start_island != split_island[nx][ny]:
                    # print("다른 섬 만났어")
                    end_island = split_island[nx][ny]
                    break
            # print("count : ", count)
            if flag and count >= 2:
                graph.add((count, start_island, end_island))

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

island = 1
split_island = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j] == 1 and not split_island[i][j]:
            find_island(i, j, island)
            island += 1

graph = set()
visit = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if split_island[i][j] > 0:
            connect_bridge(i, j)

graph = list(graph)
graph.sort(key=lambda x : x[0])
parent = [i for i in range(island)]
tree = [False] * island

# print(graph)

answer = 0
for cost, a, b in graph:
    if tree[a] and tree[b]:
        continue
    union_parent(a, b)
    answer += cost
    tree[a] = True
    tree[b] = True
    for i in range(1, island):
        parent[i] = find_parent(i)

    # print(parent)
    if len(set(parent[1:])) == 1:
        print(answer)
        break

for i in range(1, island):
    parent[i] = find_parent(i)

if len(set(parent[1:])) > 1:
    print(-1)
