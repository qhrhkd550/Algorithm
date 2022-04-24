'''
  * 아이디어 1
    - 그리디한 방식으로 앞으로 갈 도시의 단가가 현재보다 높으면 다음 도시까지만
    - 갈 수 있는 기름을 넣고 단가를 수정한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

answer = 0
price = city[0]
flag = False
for i in range(1, n):
    if city[i] > price:
        answer += price * road[i-1]
    else:
        answer += price * road[i-1]
        price = city[i]
    
print(answer)
