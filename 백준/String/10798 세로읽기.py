'''
* 체감 난이도 : *

* 아이디어 1
  - 최대 문자열 길이만큼 공백으로 채운다
  - zip 함수를 이용해 행과 열을 바꾼다
  - answer에 추가하면서 공백은 지운다
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

board = [list(map(str, input())) for _ in range(5)]

max_len = 0
for i in range(5):
    if max_len < len(board[i]):
        max_len = len(board[i])

for i in range(5):
    if len(board[i]) < max_len:
        for _ in range(max_len - len(board[i])):
            board[i].extend(' ')

answer = ''
for b in zip(*board):
    answer += ''.join(b)

print(answer.replace(" ", ""))