'''
  * 아이디어 1
    - A와 B의 자리수를 구한 후, 해당 자리수에서 4와 7로 만들 수 있는 모든 수를 구한다.
    - 해당 수가 A와 B 사이의 값이라면 answer + 1 한다.

'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import product

A, B = map(int, input().split())
answer = 0
for i in range(len(str(A)), len(str(B))+1):
    pro = list(product([4, 7], repeat=i))
    for num in pro:
        n = int(''.join(map(str, num)))
        if A <= n <= B:
            answer += 1
print(answer)
