import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))



def bellman_ford(start):
    dist[start] = 0

    for i in range(1, n+1):
        for j in range(m):
            now, next, cost = graph[j][0], graph[j][1], graph[j][2]
            if dist[now] != float('inf') and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                if i == n:
                    return True

    return False

dist = [float('inf')] * (n+1)
if bellman_ford(1):
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])