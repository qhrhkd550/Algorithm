import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]

meeting = sorted(meeting, key=lambda x : (x[1], x[0]))

ns, ne = meeting[0]
count = 1
for start, end in meeting[1:]:
    if start < ne:
        continue
    ns, ne = start, end
    count += 1

print(count)