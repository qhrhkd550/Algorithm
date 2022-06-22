from collections import deque, defaultdict
import sys
input = lambda : sys.stdin.readline().rstrip()


n, k = map(int, input().split())
water = list(map(int, input().split()))
# 집을 k개만큼 설치하고 각 집에서 샘터까지의 최소거리의 합을 구한다. -> DFS로 해결해야하는데 재귀횟수가 1000을 초과한다.
# 각 샘터에서 방문하지 않은 포인트를 탐색해 나간다.
# bfs 방문 시 집 설치 위치에는 제약조건이 없기 때문에 범위체크를 하지 않는다.

def bfs():
    answer = 0
    count = 0

    while q:
        qlen = len(q)
        while qlen:
            x = q.popleft()
            for i in [x-1, x+1]:
                # if i < 0 or i >= 200000001:
                #     continue

                if visit[i] != -1:
                    continue

                visit[i] = visit[x] + 1
                q.append(i)
                answer += visit[i]
                count += 1

                if count == k:
                    return answer

            qlen -= 1

visit = defaultdict(lambda : -1)
q = deque()
for w in water:
    i = 100000000 + w
    q.append(i)
    visit[i] = 0


print(bfs())