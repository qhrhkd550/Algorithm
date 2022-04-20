'''
* 아이디어 1
  - 길이가 1이 될때까지 토너먼트를 수행한다.
  - 팁! 그냥 순서대로 더해도 문제에서 요구하는 값이 나온다. 즉, for문 한번으로 해결 가능
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

string = input()
mapping = {}
for alpha, num in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]):
    mapping[alpha] = num

start = []
for s in string:
    start.append(mapping[s])

length = len(start)
while True:
    new = []
    for i in range(0, length, 2):
        if i == length:
            break
        elif i == length-1:
            new.append(start[i])
        else:
            new.append(start[i] + start[i+1])
    if len(new) == 1:
        if new[0] % 2 != 0:
            print("I'm a winner!")
        else:
            print("You're the winner?")
        break
    start = new.copy()
    length = len(start)

