def solution(n, s, a, b, fares):
    answer = float('inf')

    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for x, y, c in fares:
        graph[x][y] = c
        graph[y][x] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                else:
                    graph[i][j] = 0

    for i in range(1, n + 1):
        if answer > graph[s][i] + graph[i][a] + graph[i][b]:
            answer = graph[s][i] + graph[i][a] + graph[i][b]

    return answer