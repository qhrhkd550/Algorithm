'''
* 문제 유형 : bfs

* 체감 난이도 : *

* 아이디어 1
  - 최소 거리를 요구하는 문제이므로 bfs 사용
  - 각 단어의 방문 여부를 딕셔너리로 관리
  - 딕셔너리의 키는 각 단어가 되고, 해당 키에 대한 값은 몇번째에 방문했는지를 나타낸다.
  
'''

from collections import deque, defaultdict

def solution(begin, target, words):
    answer = 0
    
    visit = defaultdict(int)
    
    def check(now_word, next_word):
        count = 0
        for n1, n2 in zip(now_word, next_word):
            if n1 != n2:
                count += 1
            if count >= 2:
                return False
        return True
        
        
    def bfs(begin):
        q = deque()
        q.append(begin)
        visit[begin] = 1
        
        while q:
            now = q.popleft()
            for i in range(len(words)):
                if check(now, words[i]) and visit[words[i]] == 0:
                    visit[words[i]] += visit[now] + 1
                    q.append(words[i])
    
    bfs(begin)
    if target in visit:
        answer = visit[target] - 1
    else:
        answer = 0
    return answer
