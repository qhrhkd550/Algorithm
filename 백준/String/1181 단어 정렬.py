'''
  * 아이디어 1
    - 중복된 단어를 제거하기 위해 set을 사용한다.
    - 조건에 맞게 정렬한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = set(input() for _ in range(n))

data = sorted(data, key=lambda x : (len(x), x))
for d in data:
    print(d)