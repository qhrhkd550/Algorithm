'''
  * 아이디어 1
    - 최대힙을 사용하기 위해 heapq 를 사용한다.
    - 큐의 길이가 3이상이라면 2번은 answer에 추가하고 한번은 그냥 값만 제거한다.
    - 만약 길이가 3 미만이라면 전부 answer에 추가한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

n = int(input())
price = []
for _ in range(n):
    heapq.heappush(price, -int(input()))

answer = 0
while True:
    if len(price) >= 3:
        for _ in range(2):
            answer += -heapq.heappop(price)
        heapq.heappop(price)

    else:
        length = len(price)
        for _ in range(length):
            answer += -heapq.heappop(price)
        break
print(answer)