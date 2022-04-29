'''
  * 아이디어 1
    - dp[i] : i번째 계단에서의 최댓값
    - i번째 최대값은 i-3, i-2번째 계단을 밟고 i를 밟는 경우와 i-3을 밟고 i-1, i를 밟는 경우 중 최대값이 된다.
    - 즉 dp 테이블을 사용하게 되면 
      - i-3, i-2번째 계단을 밟고 i를 밟는 경우 -> i-3, i-2를 밟는 경우는 dp[i-2]와 같다. 즉, dp[i-2] + score[i]
      - i-3을 밟고 i-1, i를 밟는 경우 -> dp[i-3] + score[i-1] + score[i]
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))

dp = [0] * n
if n >= 1:
    dp[0] = score[0]
if n >= 2:
    dp[1] = score[0] + score[1]
if n >= 3:
    dp[2] = max(score[0] + score[2], score[1] + score[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

print(dp[-1])