'''
  * 아이디어 1
    - dp 테이블은 data값으로 초기화 한다.
    - 현재 인덱스보다 작은 인덱스 중, 값이 작은 포인트에 대해 data[i] + dp[j] > dp[i]이면 dp[i]를 업데이트한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))

dp = [i for i in data]

for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            if data[i] + dp[j] > dp[i]:
                dp[i] = data[i] + dp[j]

print(max(dp))