import sys
input = lambda : sys.stdin.readline().rstrip()

board = input()
board = board.replace("XXXX", "AAAA").replace("XX", "BB")
if "X" in board:
    print(-1)
else:
    print(board)
