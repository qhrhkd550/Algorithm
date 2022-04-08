'''
* 체감 난이도 : *****

* 아이디어 1
  - mCn 조합의 수를 factorial로 구현하여 해결

* 풀이 1
  - 파스칼 삼각형을 이용해 dp 테이블을 만들어 해결할 수 있다.
  - nCr = nCr-1 + n-1Cr-1
'''
# import sys
# input = lambda : sys.stdin.readline().rstrip()
#
# t = int(input())
#
# def factorial(n):
#     if n == 1:
#         return n
#     return n * factorial(n-1)
#
# for _ in range(t):
#     n, m = map(int, input().split())
#     if n == m:
#         print(1)
#
#     elif n == 1:
#         print(m)
#
#     else:
#         answer = factorial(m) // (factorial(n) * factorial(m-n))
#         print(answer)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1:
                dp[i][j] = j
            elif i == j:
                dp[i][j] = 1
            else:
                if j > i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[n][m])