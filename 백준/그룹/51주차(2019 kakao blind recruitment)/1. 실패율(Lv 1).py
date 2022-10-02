from collections import defaultdict


def solution(N, stages):
    answer = []

    result = defaultdict()

    for i in range(1, N + 1):
        try_count = 0
        not_clear = 0
        for j in range(len(stages)):
            if stages[j] > i:
                try_count += 1
            elif stages[j] == i:
                try_count += 1
                not_clear += 1

        if try_count > 0:
            result[i] = not_clear / try_count
        else:
            result[i] = 0

    result = sorted(result.items(), key=lambda x: -x[1])
    for x, y in result:
        answer.append(x)

    return answer