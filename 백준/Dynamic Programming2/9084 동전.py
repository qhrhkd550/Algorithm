'''
  * 아이디어 1
    - 동전이 오름차순으로 정렬되어 있기 때문에 각 동전을 사용해서 만들 수 있는 경우의 수를 누적시켜나간다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    target = int(input())

    data = [0] * (target+1)
    data[0] = 1 # 사용하지않는 0번째를 1로 설정함으로써, 코인과 같은 인덱스라면 1을 추가하게 한다.
    for c in coin:
        for i in range(1, target+1):
            if i >= c:
                data[i] += data[i-c]

    print(data[target])