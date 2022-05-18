'''
  * 아이디어 1
    - 매번 절반을 버려야 하기 때문에 가장 용량이 큰 에너지드링크에 나머지를 절반씩 섞으면 된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
energy = list(map(int, input().split()))
energy.sort(reverse=True)
answer = energy[0]
for i in range(n-1, 0, -1):
    answer += energy[i]/2

print(answer)