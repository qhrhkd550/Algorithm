'''
* 체감 난이도 : **

* 아이디어 1
  - 1개 또는 3개씩 돌을 가져갈 수 있으므로 첫번째 사람이 항상 홀수번째를 가져갈 수 있다.
  - 반대로 항상 두번째 사람이 짝수번째를 가져간다.
  - 따라서 홀짝에 따라 승자를 정하면 된다.

'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
if n % 2 == 0:
    print("CY")
else:
    print("SK")
