from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        max_value, max_menu = 0, []

        for order in orders:
            com = combinations(sorted(order), c)
            max_menu.extend(com)

        count = Counter(max_menu)
        if count:
            max_value = max(count.values())
            if max_value >= 2:
                for key, value in count.items():
                    if max_value == value:
                        answer.append(''.join(key))
    answer.sort()
    return answer