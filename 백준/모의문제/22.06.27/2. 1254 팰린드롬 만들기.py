import sys
input = lambda : sys.stdin.readline().rstrip()

S = input()

for i in range(len(S)):
    tmp = S[i:]
    if tmp == tmp[::-1]:
        print(len(S) + i)
        break