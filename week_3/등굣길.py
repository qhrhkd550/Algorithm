'''
* 문제 유형 : DP

* 체감 난이도 : **

* 아이디어 1
  - 2차원 좌표계에서 경로 개수 구하는 문제와 동일
  - 물 웅덩이인곳만 고려해서 경로를 계산
  - 단, pubbles의 좌표가 y, x 이므로 해당 부분을 고려해야함
'''

def solution(m, n, puddles):
    answer = 0
    
    dp = [[0] * m for _ in range(n)]
    for x, y in puddles:
        dp[y-1][x-1] = -1
    
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if dp[i][j] != -1:
                if i - 1 >= 0:
                    if dp[i-1][j] != -1:
                        dp[i][j] += dp[i-1][j]
                if j - 1 >= 0:
                    if dp[i][j-1] != -1:
                        dp[i][j] += dp[i][j-1]
                    
    answer = dp[n-1][m-1] % 1000000007
    
    return answer
