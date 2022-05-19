'''
  * 아이디어 1
    - 가치가 큰 동전부터 사용할 수 있는만큼 사용하면 된다.
    - 직접 계산할 수도 있지만 몫과 나머지를 이용하면 간단하다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

coin.sort(reverse=True)

answer = 0
for c in coin:
    if k == 0:
        break
    if c > k:
        continue

    p, v = divmod(k, c)
    k = v
    answer += p

print(answer)