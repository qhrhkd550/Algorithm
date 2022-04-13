'''
* 체감 난이도 : ***

* 아이디어 1
  - 문제에 주어진 순서대로 따라가면 되는 문제이다.
  - 조심할점은 구름을 이동시킬때는 좌표끼리 연결되어있지만, 대각선 방향을 체크할 때는 범위안의 점만 체크해야 한다는 점이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)] # 처음 구름이 생기는 곳
for _ in range(m):
    d, s = map(int, input().split())

    # 1 구름의 좌표를 옮겨주고
    for i in range(len(cloud)):
        cloud[i] = ((cloud[i][0] + dx[d-1]*s)%n, (cloud[i][1] + dy[d-1]*s)%n)

    # 2 옮겨진 곳에 1씩 더한다
    for x, y in cloud:
        data[x][y] += 1

    # 3 & 4 각 구름별로 대각선 방향을 확인해 바구니에 물이 찬 지점 개수만큼 증가
    for i in range(len(cloud)):
        count = 0
        for j in [1,3,5,7]: # 대각선
            nx = cloud[i][0] + dx[j]
            ny = cloud[i][1] + dy[j]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] > 0:
                count += 1
        data[cloud[i][0]][cloud[i][1]] += count

    # 5 새롭게 구름이 생성될 곳을 new_cloud에 정한다.
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in cloud and data[i][j] >= 2: # 현재 구름위치가 아니고 2 이상이라면 -2 시켜주고, 새로운 구름 위치에 저장
                data[i][j] -= 2
                new_cloud.append((i, j))

    cloud = new_cloud # 구름 위치를 업데이트

answer = 0
for d in data:
    answer += sum(d)
print(answer)