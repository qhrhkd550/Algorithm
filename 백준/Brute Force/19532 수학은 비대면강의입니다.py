'''
* 아이디어 1
  - 연립방정식을 풀기보다는 유일한 해만 존재하고 x, y의 범위가 주어져있으므로 모든 경우에 대해서 두 방정식에 대입해본다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

a, b, c, d, e, f = map(int, input().split())

def search():
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a*x + b*y == c and d*x + e*y == f:
                print(x, y)
                return

search()