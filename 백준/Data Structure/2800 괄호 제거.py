'''
  * 아이디어 1
    - 괄호의 위치(인덱스)를 뽑아내서 쌍으로 정보를 가지고 있는다.
    - 괄호 쌍을 가지고 괄호를 몇개 쓸껀지 정하기 위해 combination을 수행한다.
    - 이때 괄호가 없는 상태에서 괄호를 더해가도 되고, 입력 받은 초기상태에서 괄호를 없애가도 무방하다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations

string = input()
stack = []
data = []
answer = set()

for i in range(len(string)):
    if string[i] == '(':
        stack.append(i)
    elif string[i] == ')': # 괄호 쌍을 만나면 data에 추가
        data.append((stack.pop(), i))

for i in range(1, len(data)+1): # 괄호 쌍을 몇개 없앨건지 결정하기 위해 1부터 문자열 길이만큼 
    for com in combinations(data, i): # combinations을 수행한다.
        new = list(string) # 초기 문자열을 리스트로 가져오고
        for c in com: # 해당 좌표의 값을 ''로 만들어 준다.
            new[c[0]] = ''
            new[c[1]] = ''
        answer.add(''.join(new)) # 괄호를 없애고 난 후의 문자열을 answer에 추가해준다.

answer = sorted(answer)
for a in answer:
    print(a)
