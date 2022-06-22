'''
  * 아이디어 1
    - 최대 수를 가지기 위해서는 K앞에 많은 M이 붙어야 하고,
    - 최소 수를 가지기 위해서는 K는 항상 혼자이며 M끼리는 합쳐져야 한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

mingyeom_number = list(map(str, input()))
max_list = []
min_list = []
max_value = ""
min_value = ""

# 최대값은 K에 많은 M을 붙여야 한다.
i = len(mingyeom_number) - 1
while i >= 0:
    tmp = ""
    if mingyeom_number[i] == "K":
        tmp += "K"
        i -= 1
        while i >= 0 and mingyeom_number[i] == "M":
            tmp = "M" + tmp
            i -= 1
    else:
        tmp += "M"
        i -= 1

    max_list.append(tmp)

max_list = max_list[::-1]

# 최소값은 K는 항상 따로 떼어내고, M끼리 합쳐야한다.
i = len(mingyeom_number) - 1
while i >= 0:
    tmp = ""
    if mingyeom_number[i] == "M":
        tmp += "M"
        i -= 1
        while i >= 0 and mingyeom_number[i] == "M":
            tmp = "M" + tmp
            i -= 1

    else:
        tmp += "K"
        i -= 1

    min_list.append(tmp)

min_list = min_list[::-1]

# 각 민겸수를 십진수로 변환
for max_ in max_list:
    tmp = ""
    if "K" in max_:
        tmp += "5"
        tmp += "0" * (len(max_) - 1)
    else:
        tmp += "1"
    max_value += tmp

for min_ in min_list:
    tmp = ""
    if "M" in min_:
        tmp += "1"
        tmp += "0" * (len(min_) - 1)
    else:
        tmp += "5"
    min_value += tmp

print(max_value)
print(min_value)
