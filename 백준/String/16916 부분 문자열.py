'''
  * 아이디어 1
    - KMP 알고리즘을 사용하면 된다.
    - KMP 알고리즘의 시간복잡도는 O(n)이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

S = input()
P = input()

j, i = 0, 1
table = [0] * len(S)
while i < len(S):
    if S[i] == S[j]:
        table[i] = j+1
        i += 1
        j += 1
    else:
        if j != 0:
            j = table[j-1]
        else:
            table[i] = 0
            i += 1

j = 0
flag = False
for i in range(len(S)):
    while j > 0 and S[i] != P[j]:
        j = table[j-1]

    if S[i] == P[j]:
        if j == len(P) - 1:
            flag = True
            break
        else:
            j += 1

if not flag:
    print(0)
else:
    print(1)

