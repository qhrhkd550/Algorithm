import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    answer = 1
    while True:
        now = queue[0]
        flag = False
        for i in range(len(queue)):
            if queue[i] > now:
                queue.pop(0)
                queue.append(now)
                m -= 1
                if m < 0:
                    m += len(queue)
                flag = True
                break

        if not flag:
            if m == 0:
                print(answer)
                break
            else:
                answer += 1
                m -= 1
                queue.pop(0)