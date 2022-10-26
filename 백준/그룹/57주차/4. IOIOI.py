N = int(input())
M = int(input())
S = input()

cursor, count, result = 0, 0, 0

while cursor < (M - 1):
    if S[cursor:cursor + 3] == 'IOI': #3칸
        count += 1
        cursor += 2
        if count == N:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0

print(result)