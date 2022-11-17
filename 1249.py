# SW Expert Academy 1249: [S/W 문제해결 응용] 4일차 - 보급로(D4)

from collections import deque

# U, D, L, R
dx = [-1, +1, +0, +0]
dy = [+0, +0, -1, +1]

def in_range(N, x, y):
    return 0 <= x < N and 0 <= y < N

def bfs(graph, result, N):
    dq = deque()
    dq.append([0, 0])

    while dq:
        cx, cy = dq.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if in_range(N, nx, ny):
                next_time = result[cx][cy] + graph[nx][ny]
                if next_time < result[nx][ny]:
                    result[nx][ny] = next_time
                    dq.append([nx, ny])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input())))
    result = [[int(1e9) for _ in range(N)] for _ in range(N)]
    result[0][0] = 0
    bfs(graph, result, N)

    print('#' + str(test_case) + ' ' + str(result[N-1][N-1]))