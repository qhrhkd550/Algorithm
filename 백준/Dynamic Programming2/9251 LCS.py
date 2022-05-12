'''
  * 아이디어 1
    - s1 : ACAYKP, s2 : CAPCAK
    - dp :  0 C A P C A K
          0 0 0 0 0 0 0 0
          A 0
          C 0
          A 0
          Y 0
          K 0
          P 0
    - 초기 dp배열은 위와 같다.
    - 모든 좌표를 탐색하여 값을 채워나가는데 식은 다음과 같다.
    - if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    - 대각선에서 가져오는 경우는 두 문자가 같기 때문에 두 문자를 모두 안쓴 자리의 값을 가져오는 것이다.
    - 위나 왼쪽에서 가져오는 경우는 두 문자가 다르기 때문에 어느 한쪽만 사용했을 때의 최대값을 가져오는 것이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

s1 = input()
s2 = input()

dp = [[0] * (len(s2)+1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(s1)][len(s2)])
