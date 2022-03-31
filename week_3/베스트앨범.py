'''
* 문제 유형 : 구현

* 체감 난이도 : **

* 아이디어 1
  - 장르별로 total play time을 관리하고, id별 play time을 list로 관리
  - 장르별로 play time이 많은 순서대로, 같다면 id가 작은 순서대로 정렬
  - 장르별 total play time이 많은 순서대로 
'''

def solution(genres, plays):
    answer = []
    
    data = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in data:
            data[genre] = {'total' : play,
                          'id' : [[i, play]]}
        else:
            data[genre]['total'] += play
            data[genre]['id'].append([i, play])
    
    for key in data.keys():
        data[key]['id'] = sorted(data[key]['id'], key=lambda x : (-x[1], x[0]))
        
    data = sorted(data.items(), key=lambda x : -x[1]['total'])
    
    for i in range(len(data)):
        if len(data[i][1]['id']) == 1:
            answer.append(data[i][1]['id'][0][0])
        else:
            for j in range(2):
                answer.append(data[i][1]['id'][j][0])
        
    return answer
