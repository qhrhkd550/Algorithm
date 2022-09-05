import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
k = 0
move = []
def hanoi(n, from_pos, to_pos, aux_pos):
    global k
    k += 1
    if n == 1:
        # print(from_pos, to_pos)
        move.append((from_pos, to_pos))
        return

    hanoi(n-1, from_pos, aux_pos, to_pos)
    move.append((from_pos, to_pos))
    # print(from_pos, to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)

hanoi(n, 1, 3, 2)

print(k)
for x, y in move:
    print(x, y)