import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
count = 0

def factorical(n):
    if n > 1:
        return n * factorical(n-1)
    else:
        return 1

num = str(factorical(n))
for i in range(len(num)-1, -1, -1):
    if num[i] != '0':
        print(count)
        break
    else:
        count += 1