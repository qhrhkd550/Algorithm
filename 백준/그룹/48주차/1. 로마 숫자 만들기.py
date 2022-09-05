import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50}
roma = ['I', 'V', 'X', 'L']
answer = set()

def dfs(path, begin):
    global answer

    if len(path) == n:
        tmp = 0
        for _ in range(n):
            tmp += data[path[_]]

        answer.add(tmp)

        return

    for i in range(begin, 4):
        dfs(path + [roma[i]], i)

visit = {'I' : False, 'V' : False, 'X' : False, 'L' : False}
dfs([], 0)

print(len(answer))