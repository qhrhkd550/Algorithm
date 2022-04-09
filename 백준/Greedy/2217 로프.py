import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort()
answer = 0
for i in range(n):
    answer = max(answer, rope[i] * (n-i))
print(answer)