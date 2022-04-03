'''
* 체감 난이도 : **

* 아이디어 1
  - 시간 계산만 하면 된다.
  - 두 시간의 차이가 0일경우 24시간을 기다려야하는 점에 주의!
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

ch, cm, cs = map(int, input().split(":"))
bh, bm, bs = map(int, input().split(":"))

current_s = cs + (cm * 60) + (ch * 3600)
boom_s = bs + (bm * 60) + (bh * 3600)

diff = boom_s - current_s
if diff <= 0:
    diff = 24*3600 + diff

hh = diff // 60 // 60
mm = diff // 60 % 60
ss = diff % 60
print(str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2))