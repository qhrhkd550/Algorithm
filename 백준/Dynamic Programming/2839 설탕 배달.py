'''
* 체감 난이도 : ***

* 아이디어 1
  - 3과 5로 만들 수 없는 수의 경우 -1로 초기화
  - dp[i] = min(dp[i-3] + 1, dp[i-5] + 1) 즉, 3을 하나 추가해서 만들 수 있는 경우와 5를 하나 추가해서 만들 수 있는 경우 중, 최소값으로 결정한다.
  - 단, i-5를 보기 위해서는 i가 5보다 커야하며, 만들 수 없는 수를 뜻하는 -1를 필터링해야한다.
  - ex)  0   1  2  3  4  5  6   7  8  9  10
        -1  -1 -1  1 -1  1  2  -1  2  3  2
        이런 상황에서 11의 경우 8을 만들기위해 2개가 필요하므로 3을 하나 추가해 3개를 이용하면 만들 수 있다.
        또한, 11의 경우 6을 만들기위해 2개가 필요하므로 5를 하나 추가해 3개를 이용하면 만들 수 있다.
        즉, 두개의 최소값인 3이 11의 정답이다.

* 아이디어 2
  - 단순히 while문을 통해 구현할 수 있다.
  - 5로 나눠진다면 가장 작은 경우이므로 5로 나눈 몫을 리턴
  - 아닌 경우, 3을 한번빼고 다시 5로 나눠지는지 체크한다.
  - 3을 뺀 결과가 0보다 작다면 만들 수 없는 경우이므로 -1 리턴
      def count(n):
        answer = 0
        while True:
            if n % 5 == 0:
                answer += n // 5
                return answer

            n -= 3
            answer += 1
            if n < 0:
                return -1


        return answer

    print(count(n))
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

dp = [-1] * (n+1)
for i in range(3, n+1):
    if i == 3 or i == 5:
        dp[i] = 1
    else:
        if i >= 5 and dp[i-3] != -1 and dp[i-5] != -1:
            dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
        elif dp[i-3] != -1:
            dp[i] = dp[i-3] + 1
        elif i >= 5 and dp[i-5] != -1:
            dp[i] = dp[i-5] + 1
print(dp[n])