import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
color = list(map(str, input()))

color_count = {"B" : 0, "R" : 0}
prev = color[0]
color_count[color[0]] += 1

for i in range(1, n):
    if prev != color[i]:
        color_count[color[i]] += 1
        prev = color[i]

color_count = sorted(color_count.items(), key=lambda x : x[1])
print(color_count[0][1] + 1)