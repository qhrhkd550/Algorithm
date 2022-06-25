'''
  * 아이디어 1
    - n = 가로로 자른 횟수 + 세로로 자른 횟수
    - 조각 개수 = (가로로 자른 횟수 + 1) * (세로로 자른 횟수 + 1)
    - 가로를 알면 세로는 n - 가로 이므로 가로를 기준으로 이분탐색한다.
    - 조각의 개수가 원하는 수보다 많다면 가로로 자르는 횟수를 줄이고 아니면 늘린다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())

start, end = 0, n
flag = False
while start <= end:
    row_cut = (start + end) // 2
    col_cut = n - row_cut

    pieces = (row_cut + 1) * (col_cut + 1)
    if k == pieces:
        flag = True
        print("YES")
        break

    if pieces > k:
        end = row_cut - 1
    else:
        start = row_cut + 1

if not flag:
    print("NO")