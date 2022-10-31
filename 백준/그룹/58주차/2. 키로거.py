import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    log = input()
    left, right = [], []
    cursor = 0
    for l in log:
        if l == '<' and left:
            right.append(left.pop())
        elif l == '>' and right:
            left.append(right.pop())
        elif l == '-' and left:
            left.pop()
        elif l.isalpha() or l.isalnum():
            left.append(l)

    print(''.join(left) + ''.join(reversed(right)))