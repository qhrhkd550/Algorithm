import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations_with_replacement

n = int(input())
answer = set()
for combination in combinations_with_replacement([1, 5, 10, 50], n):
    answer.add(sum(combination))

print(len(answer))