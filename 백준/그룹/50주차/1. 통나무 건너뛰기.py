import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    L = list(map(int, input().split()))

    L.sort()
    tmp = [0] * len(L)
    l, r = 0, len(L)-1
    for i in range(len(L)):
        if i % 2 == 0:
            tmp[l] = L[i]
            l += 1
        else:
            tmp[r] = L[i]
            r -= 1

    answer = 0
    for i in range(len(L)):
        if i == len(L)-1:
            if answer < abs(tmp[i] - tmp[0]):
                answer = abs(tmp[i] - tmp[0])
        else:
            if answer < abs(tmp[i] - tmp[i+1]):
                answer = abs(tmp[i] - tmp[i+1])

    print(answer)