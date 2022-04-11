'''
* 체감 난이도 : ***

* 아이디어 1
  - 현재 수보다 작은 수 중에 완전 제곱수를 찾는다.
  - dp[현재 수 - 찾은 완전 제곱수] 값이 최소인 완전 제곱수를 찾는다.
  - 어짜피 완전제곱수는 수가 하나만 필요하므로 dp[현재 수 - 찾은 완전 제곱수]값이 최소인 지점을 찾으면 된다.
  - ex) i = 10 -> 완전 제곱수는 1, 4, 9가 존재한다.
  - 1일때, dp[9] = 1
  - 4일때, dp[6] = 3
  - 9일때, dp[1] = 1 이므로 최소값인 1 + 완전제곱수를 만들기위해 필요한 수 1 = 2가 dp[10] 의 값이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
import math

n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    min_value = int(1e9)
    for k in range(1, int(math.sqrt(i)) + 1):
        min_value = min(min_value, dp[i - k*k])
    dp[i] = min_value + 1
print(dp[n])