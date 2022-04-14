'''
* 아이디어 1
  - 홀수를 k개 만큼 지울 수 있다는 것은 무시하고 지나가도 된다는 뜻이다. 실제로 지우게 되면 시간이 오래걸린다.
  - k > -1 인 이유는, k가 0이 되는 순간 멈춰버리면 다음에 등장하는 수가 짝수일지라도 최대 길이에 포함하지 않기 때문이다.
  - data[end]를 반복적으로 보며 홀수인 경우 k -= 1, 짝수인경우 count += 1을 수행한다.
  - 하나의 start에 대해서 end작업을 끝냈다면, start 또한 홀수인 경우 k += 1, 짝수인 경우 count -= 1을 수행한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
data = list(map(int, input().split()))
end = 0
count = 0
max_count = 0
for start in range(n):
    while end < n and k > -1:

        if data[end] % 2 != 0:
            k -= 1
        else:
            count += 1
        end += 1

    if max_count < count:
        max_count = count


    if data[start] % 2 != 0:
        k += 1
    else:
        count -= 1

print(max_count)

