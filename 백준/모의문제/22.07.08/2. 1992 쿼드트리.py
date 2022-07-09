import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = [list(map(int, input())) for _ in range(n)]
answer = []
def check(x, y, n):
    one, zero = 0, 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] == 1:
                one += 1
            else:
                zero += 1
            if one > 0 and zero > 0:
                answer.append("(")
                return False

    if one:
        answer.append("1")
    else:
        answer.append("0")

    return True

def dfs(x, y, n):
    if check(x, y, n):
        return

    dfs(x, y, n // 2)
    dfs(x, y + n // 2, n // 2)
    dfs(x + n // 2, y, n // 2)
    dfs(x + n // 2, y + n // 2, n // 2)
    answer.append(")")
dfs(0, 0, n)
print(''.join(answer))