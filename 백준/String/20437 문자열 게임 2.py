'''
  * 아이디어 1
    - 우선 각 알파벳별로 문장에 몇 개씩 있는지 조사한다.
    - 모든 알파벳을 시작점으로 만약 해당 시작점의 알파벳이 k개가 안될 경우는 진행하지 않는다.
    - k개가 될 경우, k개를 찾을 때 까지 진행시키고 해당 위치에서 길이의 최소값과 최대값을 구한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import Counter, defaultdict

t = int(input())
for _ in range(t):
    w = input()
    k = int(input())
    w_count = Counter(w)

    data = defaultdict(list)
    question_1 = float('inf')
    question_2 = 0

    flag = False
    for start in range(len(w)):
        if w_count[w[start]] >= k:
            tmp_k = k
            end = start
            while end < len(w):
                if w[end] == w[start]:
                    tmp_k -= 1
                    if tmp_k == 0:
                        flag = True
                        question_1 = min(question_1, end - start + 1)
                        question_2 = max(question_2, end - start + 1)
                        break
                end += 1

    if not flag:
        print(-1)
    else:
        print(question_1, question_2)