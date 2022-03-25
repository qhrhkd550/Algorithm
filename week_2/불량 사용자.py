'''
* 문제 유형 : 조합, 중복 순열

* 체감 난이도 : *****

* 아이디어 1
  - '가사검색' 문제에서 bisect를 활용해 banned_id에 해당하는 리스트를 만들려고 했으나,
  - bisect를 이용할 경우, id가 한 종류의 타입으로만 이루어져야 하기 때문에 적용 불가능.(해당 문제는 소문자와 숫자로 이루어짐)
  
* 아이디어 2
  - 주어진 id의 개수가 적기 때문에, 완전 탐색으로 banned_id별 매칭되는 user_id를 저장 (id_list)
  - banned_id가 같을수도 있기 때문에, banned_id 별로 몇개씩 나왔는지도 저장 (ban_count)
  - 중복된 banned_id는 조합으로 처리 즉, 해당 banned_id가 포함된 user_id에서 중복된 banned_id개수 만큼을 뽑는 조합
  - 나머지 banned_id는 product연산을 통해 중복을 제거하여 경우의 수 게산
  
'''

from itertools import product, combinations
from collections import defaultdict

def solution(user_id, banned_id):
    answer = 1
    
    def check(ban, user):
        for b, u in zip(ban, user):
            if b == "*":
                continue
            if b != u:
                return False
            
        return True
            
    id_list = defaultdict(list)
    ban_count = defaultdict(int)
    for ban in banned_id:
        ban_count[ban] += 1
        for user in user_id:
            if len(ban) == len(user):
                if check(ban, user) and user not in id_list[ban]:
                    id_list[ban].append(user)
    
    for key, value in ban_count.items():
        if value >= 2: # 중복된 ban이 있다면 먼저 조합으로 처리하고 id_list에서 제거
            answer *= len(list(combinations(id_list[key], value)))
            del id_list[key]

    p = set(product(*id_list.values())) # 나머지 ban에 대해 product연산을 수행하고 같은 경우를 제거
    p = [list(p_) for p_ in p if len(set(p_)) == len(id_list)] # 각 경우에서 중복된 id를 뽑은 경우도 제거
    for i in range(len(p)): # 현재 가능한 모든 경우에 대해 (a, b) 는 (b, a)와 같은 경우이므로, sort하여 다시 저장
         p[i] = tuple(sorted(p[i])) 
    p = set(p) # (a, b), (b, a) -> (a, b), (a, b)가 되므로 중복 제거
    
    answer *= len(p)
                
    return answer
