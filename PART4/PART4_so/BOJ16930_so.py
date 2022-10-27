# BOJ16930_달리기

from collections import deque

N, M, K = map(int, input().split())

graph = []
for _ in range(N):
    temp = input()
    graph.append(list(temp))

visited = [[-1 for _ in range(M)] for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def can_go(x, y):
    if not in_range(x, y):
        return False
    if graph[x][y] == '#':
        return False
    return True


def bfs(sx, sy):
    global graph, visited
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 0

    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

    while q:
        x, y = q.popleft()

        if x == x2-1 and y == y2-1:
            return visited[x][y]

        for dx, dy in zip(dxs, dys):
            for k in range(1, K+1): #갈 수 있는 최대 k만큼의 방향까지 간다
                nx, ny = x + dx * k, y + dy * k
                
                if can_go(nx, ny) and visited[nx][ny] == -1:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1  # 이전 길에서 *k만큼 갔을 때를 표시
                    
                elif can_go(nx, ny) and visited[nx][ny] == visited[x][y] + 1:
                    continue  # 이미 간 길은 continue
                  
                else:
                    break  # 더 큰 길은 탐색 안 함
    return -1


print(bfs(x1 - 1, y1 - 1))


'''
최소시간이니까 bfs
최대개수 k까지 이동 가능
'''
