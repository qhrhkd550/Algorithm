import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
data = list(map(int, input()))
answer = []
for i in range(n):
    if not answer:
        answer.append(data[i])
    else:
        while answer and k > 0 and answer[-1] < data[i]:
            k -= 1
            answer.pop(-1)

        answer.append(data[i])

if k > 0:
    answer = answer[:-k]

for a in answer:
    print(a, end = '')
