'''
* 체감 난이도 : ***

* 아이디어 1
  - 한 round당 game을 생성 후, 해당 game 으로 외쳐야 할 구호가 나오면 t를 마이너스 시킨다.
  - game이 계속 반복될때마다 num(자리수)은 0~a-1 까지 반복한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

a = int(input())
t = int(input())
shout = int(input())

def search(t):
    num = 0
    round = 1
    while True:
        game = '0101' + '0'*(round+1) + '1'*(round+1)
        for g in game:
            if int(g) == shout:
                t -= 1
                if t == 0:
                    print(num)
                    return
            num += 1
            if num >= a:
                num = 0

        round += 1

search(t)