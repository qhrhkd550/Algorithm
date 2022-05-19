'''
  * 아이디어 1
    - 하루에 2개씩 사용해야하므로 근손실이 최소가 되기 위해서는 큰값, 작은값을 하나씩 골라야한다.
    - 단 운동개수가 홀수인경우, 0을 추가해서 짝수가 되도록 한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
t = list(map(int, input().split()))

muscle = sorted(t)
muscle_reverse = sorted(t, reverse=True)

answer = 0
if n % 2 != 0:
    muscle.insert(0, 0)
    muscle.append(0)

for a, b in zip(muscle, muscle_reverse):
    if answer < a + b:
        answer = a + b

print(answer)