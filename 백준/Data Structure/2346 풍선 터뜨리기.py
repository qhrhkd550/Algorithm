'''
* 아이디어 1
  - deque의 rotate를 활용한다.
  - 처음에 deque에 넣을때 enumerate를 활용하여 인덱스 정보까지 같이 생성한다.
  - 풍선의 값에따라 회전의 계산을 다르게 수행해야한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
balloon = deque(enumerate(map(int, input().split())))
answer= []

while balloon:
    index, num = balloon.popleft()
    answer.append(index+1)
    if num > 0:
        balloon.rotate(-(num-1))
    else:
        balloon.rotate(-num)

for a in answer:
    print(a, end= ' ')