import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
pillar = [list(map(int, input().split())) for _ in range(n)]

pillar.sort(key = lambda x : -x[1])

l_pivot, r_pivot = pillar[0][0], pillar[0][0]
answer = pillar[0][1]

for x, y in pillar[1:]:
    if l_pivot < x < r_pivot:
        continue

    elif x < l_pivot:
        answer += (l_pivot - x) * y
        l_pivot = x

    elif r_pivot < x:
        answer += (x - r_pivot) * y
        r_pivot = x

print(answer)
