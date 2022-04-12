'''
* 아이디어 1
  - k가 0을 포함하기 때문에 zfill함수를 통해 4분이라면 04로 표시해야 한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
k = str(k)
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if k in str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2):
                count += 1

print(count)
