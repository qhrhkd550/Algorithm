'''
* 체감 난이도 : ***

* 주의할 점!
  - n보다 작은 자연수면 정답후보가 된다. n이 4자리 수라고해서 정답도 4자리일 필요는 없다!!
  - n보다 작은 모든 수를 탐색하게되면 시간이 엄청 오래 걸린다.
  - 따라서 k 집합 안의 수로 만들 수 있는 모든 수에 대해 n보다 작은지 탐색하는게 효율적이다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import product

n, k = map(int, input().split())
data = list(map(str, input().split()))

max_value = 0
for i in range(1, len(str(n))+1):
    for pro in product(data, repeat=i):
        if int(''.join(pro)) <= n:
            if max_value < int(''.join(pro)):
                max_value = int(''.join(pro))

print(max_value)
