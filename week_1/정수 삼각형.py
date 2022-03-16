'''
* 문제 유형 : DP

* 체감 난이도 : **

* 아이디어 1
  - 위에서 부터 내려가면 index error 를 주의해야하기 때문에 아래에서부터 위로 올라오면서
  - j번째, j+1번째 값중 큰 값을 더한다
'''

def solution(triangle):
    answer = 0
    
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])
    
    return triangle[0][0]
