import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
total_people = 0
data = []
for _ in range(n):
    village, num = map(int, input().split())
    data.append((village, num))
    total_people += num

data = sorted(data, key=lambda x : x[0])

count = 0
answer = 0
for i in range(n):
    count += data[i][1]
    if count >= total_people / 2:
        answer = data[i][0]
        break
print(answer)

