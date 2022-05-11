'''
  * 아이디어 1
    - 만약 마지막 문자가 ABCDEF 안에 없다면 조건을 만족하지 않는 염색체이다.
    - 각 염색체별로 AFC의 체크를 위한 tmp를 사용한다.
    - C를 체크하기 전에는 A가 등장하면 체크, F가 등장하면 A가 True인경우에만 True, C가 등장하면 A, F가 True 인 경우에만 True이다.
    - C가 True인 순간부터는 뒤에 나오는 문자가 ABCDEF안에 있어야 하고, 만약 있다면 하나만 등장해야 한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    data = input()
    flag = False
    if data[-1] not in 'ABCDEF':
        flag = True

    else:
        i = 0
        tmp = {'A' : False, 'F' : False, 'C' : False}
        while i < len(data):
            if tmp['C']:
                if data[i] not in "ABCDEF": # C 이후에 등장하는 문자는 ABCDEF안에 있어야한다.
                    flag = True
                elif len(data) - 1 - i > 1: # C 이후에 등장하는 문자는 없거나 1개만 있어야 한다.
                    flag = True

            else:
                if data[i] in 'AFC':
                    if data[i] == 'A':
                        tmp['A'] = True

                    if data[i] == 'F': # F가 등장했다면 A는 True 상태여야한다.
                        if not tmp['A']:
                            flag = True
                            break
                        else:
                            tmp['F'] = True

                    if data[i] == 'C': # C가 등장했다면 A와 F는 True 상태여야한다.
                        if not tmp['A'] or not tmp['F']:
                            flag = True
                            break
                        else:
                            tmp['C'] = True

            i += 1

    if not flag:
        print("Infected!")
    else:
        print("Good")


