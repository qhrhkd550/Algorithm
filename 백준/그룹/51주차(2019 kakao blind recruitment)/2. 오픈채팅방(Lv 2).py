from collections import defaultdict


def solution(record):
    answer = []
    info = defaultdict()

    for r in record:
        string = r.split()
        if string[0] == "Enter" or string[0] == "Change":
            info[string[1]] = string[2]

    for r in record:
        string = r.split()
        if string[0] == "Enter":
            answer.append(info[string[1]] + "님이 들어왔습니다.")
        elif string[0] == "Leave":
            answer.append(info[string[1]] + "님이 나갔습니다.")

    return answer