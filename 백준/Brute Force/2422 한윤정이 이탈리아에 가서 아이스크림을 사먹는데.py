'''
* 아이디어 1
  - 단순하게 모든 조합 경우에 대해 맛 없는 조합(x, y)를 x not in 조합 and y not in 조합 으로 비교하면 시간초과 발생
  - 따라서, 맛 없는 조합을 연결리스트 형태로 만든다.
  - 한 조합이 나왔다면, 그 중 2개를 뽑아 연결리스트에 존재하는지 확인 후, 존재한다면 선택불가한 조합이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations

n, m = map(int, input().split())
no = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    no[a].append(b)
    no[b].append(a)

count = 0
for com in combinations(range(1, n+1), 3):
    flag = True
    for i in combinations(com, 2):
        if i[1] in no[i[0]]:
            flag = False
            break

    if flag:
        count += 1
print(count)