from itertools import combinations


def solution(relation):
    answer = 0
    attribute_len = len(relation[0])
    candidate = []
    unique = []

    for i in range(1, attribute_len + 1):
        for com in combinations(range(attribute_len), i):

            # 유일성
            tmp = [tuple([item[key] for key in com]) for item in relation]

            if len(set(tmp)) == len(relation):
                put = True

                # 최소성
                for x in unique:
                    if set(x).issubset(set(com)):
                        put = False
                        break

                if put:
                    unique.append(com)

    answer = len(unique)

    return answer