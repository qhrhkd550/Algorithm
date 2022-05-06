'''
  * 아이디어 1
    - 최대힙, 최소힙을 따로 관리한다. 이때 한쪽에서 삭제되면 그 값을 찾아서 다른 한쪽의 힙에서 삭제할 경우 프로그래머스에서는 통과되지만 백준에서는 시간초과가 발생한다.
  * 아이디어 2
    - 최대힙과 최소힙을 연결시키기 위해, visit라는 동기화 배열을 사용한다.
    - 값이 입력될 경우, visit의 해당 인덱스에 True를 표시한다.
    - 값을 삭제하는 경우, 해당 값이 가지는 인덱스를 찾아 visit에서 False 처리하면된다.
    - 이때, 최소힙에서는 삭제했지만 최대힙에서는 삭제를 안한다. 따라서, 삭제연산이 들어올 경우, False라면 True가 나올때까지 즉, 없어진값이 아닐때까지 pop시켜준다.
    - 모든 연산이 끝난 후, 마찬가지로 최소힙(최대힙)에서 지웠지만, 최대힙(최소힙)에 남아있을 수 있으므로, 위의 연산을 수행한다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq


T = int(input())
for _ in range(T):
    max_q = []
    min_q = []

    k = int(input())
    visit = [False] * k # 동기화 시키기 위한 배열

    for i in range(k):
        oper, value = map(str, input().split())
        value = int(value)

        if oper == "I":
            heapq.heappush(min_q, (value, i))
            heapq.heappush(max_q, (-value, i))
            visit[i] = True # 값이 입력될 때, True

        elif oper == "D":
            if len(max_q) == 0:
                continue

            if value == 1: # 최대값 삭제
                while max_q and not visit[max_q[0][1]]: # 최대힙에는 있지만 최소힙에서 없어진 경우를 제거하기 위해 False값을 가리키고 있다면 계속 제거
                    heapq.heappop(max_q)
                if max_q:
                    visit[max_q[0][1]] = False
                    heapq.heappop(max_q)

            elif value == -1: # 최소값 삭제
                while min_q and not visit[min_q[0][1]]: # 최소힙에는 있지만 최대힙에서 없어진 경우를 제거하기 위해 False값을 가리키고 있다면 계속 제거
                    heapq.heappop(min_q)
                if min_q:
                    visit[min_q[0][1]] = False
                    heapq.heappop(min_q)

    # 연산이 끝나고 나서도 양쪽의 균형을 맞추기 위해 실행
    while max_q and not visit[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and not visit[min_q[0][1]]:
        heapq.heappop(min_q)

    if len(max_q) == 0:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0])
