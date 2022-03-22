'''
* 문제 유형 : stack, linked_list

* 체감 난이도 : *****

* 풀이
  - i 번째 번호는 [i-1, i+1]의 정보를 가짐
  - U이나 D연산이라면 주어진 횟수만큼 link를 따라가면 됨
  - C 일 경우, k번째 노드의 정보는 그대로 유지 -> Z 연산시 사용해야하기 때문
              k-1번째 노드와 k+1번째 노드의 next와 prev를 k의 [1], [0]의 값으로 각각 매칭
  - Z 일 경우, stack의 마지막 노드의 정보를 토대로 앞과 뒤 노드의 정보 변경
  
* 주의!
  - answer 생성 시, 아래 코드는 시간초과...
    answer = ''
    for i in range(n):
      if i not in stack:
        answer += 'X'
      else:
        answer += 'O'
        
'''

def solution(n, k, cmd):
    answer = ["O" for i in range(n)]
    data = {}
    stack = []
    
    for i in range(n):
        data[i] = [i - 1, i + 1]
            
    for c in cmd:
        # U, D 연산의 경우 주어진 횟수만큼 link를 따라가면 된다.
        if "U" in c or "D" in c:
            oper, num = c.split(" ")[0], int(c.split(" ")[1])
            if oper == 'D':
                for _ in range(num):
                    k = data[k][1]
            elif oper == "U":
                for _ in range(num):
                    k = data[k][0]
                    
        elif "C" in c:
            stack.append(k)
            answer[k] = "X"
            
            if data[k][0] == -1: # -1은 가장 첫번째 노드의 prev값을 의미한다. 따라서, 이 경우 다음 노드의 prev값을 -1로 변경, k는 다음 노드가 된다.
                data[data[k][1]][0] = data[k][0]
                k = data[k][1]
            elif data[k][1] == n: # n은 가장 마지막 노드의 next값을 의미한다. 따라서, 이 경우 이전 노드의 next값을 n으로 변경, k는 이전 노드가 된다.
                data[data[k][0]][1] = data[k][1]
                k = data[k][0]
            else: # 가운데 있는 노드들의 경우 노드 정보에 따라 업데이트, k는 다음 노드가 된다.
                data[data[k][0]][1] = data[k][1]
                data[data[k][1]][0] = data[k][0]
                k = data[k][1]

        elif "Z" in c:
            z = stack.pop(-1)
            answer[z] = "O"
            
            if data[z][0] == -1: # -1은 가장 첫번째 노드의 prev값을 의미한다. 따라서, 이 경우 복구할 노드의 next 노드의 prev값을 복구 노드로 변경
                data[data[z][1]][0] = z
            elif data[z][1] == n: # n은 가장 마지막 노드의 next값을 의미한다. 따라서, 이 경우 복구할 노드의 prev 노드의 next값을 복구 노드로 변경
                data[data[z][0]][1] = z
            else: # 가운데 있는 노드들의 경우 노드 정보에 따라 업데이트
                data[data[z][0]][1] = z
                data[data[z][1]][0] = z
    
    return ''.join(answer)
