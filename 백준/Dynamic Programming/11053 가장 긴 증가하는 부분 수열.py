'''
  * 아이디어 1
    - 10, 20, 10, 30, 20, 50 일때, 만약 30을 본다 가정하면,
    - 30보다 앞에있고 값이 작은 10, 20, 10의 dp값을 확인하고, dp값이 더 크다면 해당 dp값을 가져오고 +1한다.
    - 즉, 10의 경우 첫번째 원소이므로 dp값은 1이 되고, 20의 경우 자신보다 앞에있고 값이 작은 10의 dp값을 비교한다. 현재 20의 dp값은 0으로 더 작기때문에
    - 20의 dp값을 10의 dp값 + 1 로 가져온다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
A = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
