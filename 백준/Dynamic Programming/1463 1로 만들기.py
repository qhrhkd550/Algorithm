'''
* 체감 난이도 : ***

* 아이디어 1
  - 총 3가지의 연산이 가능하다. 3으로 나누기, 2로 나누기, 1 빼기
  - dp 테이블을 생성하고 각 연산을 수행했을때 dp테이블의 값이 최소인 값을 찾는다.
  - ex) n = 4 -> dp[3] = 1 (-1 연산)
                 dp[2] = 1 (//2 연산)
                 4는 3의 배수가 아니므로 //3 은 수행하지 않는다.
                 따라서 dp[4] = 3가지 연산 중 최소값 1 + 1 = 2가 된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dp = [0] * (n+1)
dp[1] = 0

for i in range(2, n+1):
    two = dp[i // 2] if i % 2 == 0 else int(1e9)
    three = dp[i // 3] if i % 3 == 0 else int(1e9)
    dp[i] = min(dp[i-1], two, three) + 1

print(dp[n])
