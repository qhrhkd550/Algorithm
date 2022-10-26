import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

n, m = map(int, input().split())
data = defaultdict(str)

for _ in range(n):
    site, passwd = map(str, input().split())
    data[site] = passwd

for _ in range(m):
    find_site = input()
    print(data[find_site])
