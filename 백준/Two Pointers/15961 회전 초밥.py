'''
* 아이디어 1
  - 먹은 초밥은 defaultdict으로 관리한다.
  - 원형 큐 이므로 end의 범위를 제한하지 않고, %n 연산으로 계속 돌아갈 수 있게 한다.
  - 모든 start 좌표에서 시작하여 k개씩 보는데 먹은 개수가 최대가 되는 값을 저장한다.
  - 하나의 start에서 k개를 봤다면 start + 1을 위해 dict의 start 값을 1 빼는데 이때 값이 0이된다면 dict에서 start를 제거한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict
n, d, k ,c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))

end = 0
eat = defaultdict(int)
eat[c] = 1
max_eat = 0
for start in range(n):
    while k > 0:
        eat[sushi[end % n]] += 1
        end += 1
        k -= 1
    if max_eat < len(eat):
        max_eat = len(eat)

    eat[sushi[start]] -= 1
    if eat[sushi[start]] == 0:
        del eat[sushi[start]]

    k += 1

print(max_eat)
