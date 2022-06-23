'''
  * 아이디어 1
    - n개의 노드를 가지는 경우부터 n-1개를 가지는 경우, n-2개를 가지는 경우, ..., 1개를 가지는 경우에 대해 각각 dfs를 수행하게되면 시간초과가 발생한다.
    - 따라서 해당 인덱스의 값 정보를 edge로 사용하여 그래프를 형성 후, 사이클이 발생하는 모든 노드들이 정답이 된다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    edge = int(input())
    graph[i].append(edge)

answer = []

def dfs(now, path):
    for next in graph[now]:
        if not visit[next]:
            visit[next] = True
            dfs(next, path+[next])
            visit[next] = False

            return

        while path:
            node = path.pop()
            answer.append(node)
            if node == next:
                break

        return

visit = [False] * (n+1)
for i in range(1, n+1):
    dfs(i, [])

answer = sorted(list(set(answer)))
print(len(answer))
for a in answer:
    print(a)